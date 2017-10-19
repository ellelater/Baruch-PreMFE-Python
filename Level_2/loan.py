from asset import Asset


class Loan(object):
    def __init__(self, term, rate, face, asset):
        if not isinstance(asset, Asset):
            print "asset parameter needs to be Asset type."
            return
        self._term = term
        self._rate = rate
        self._face = face
        self.asset = asset
        self._pmt_per_month = self._rate * self._face / (1 - (1 + self._rate)**(-self._term))

    def monthlyPayment(self, period):
        return self._pmt_per_month

    def totalPayments(self):
        return sum([self.monthlyPayment(period) for period in range(self._term)])

    def totalInterest(self):
        return self.totalPayments() - self._face

    def interestDue(self, period):
        if period <= 0:
            return 0
        return self.balance(period - 1) * self._rate

    def principalDue(self, period):
        return self.monthlyPayment(period) - self.interestDue(period)

    def balance(self, period):
        return self._face * (1 + self._rate) ** period - self.monthlyPayment(period) * ((1 + self._rate) ** period - 1) / self._rate

    def recoveryValue(self, period):
        return self.asset.current_val(period) * 0.6  # recovery multiplier

    def equity(self, period):
        return self.asset.current_val(period) - self.balance(period)


class FixedRateLoan(Loan):
    def __init__(self, term, rate, face, asset):
        super(FixedRateLoan, self).__init__(term, rate, face, asset)


class VariableRateLoan(Loan):
    def __init__(self, term, rate, face, rate_dict, asset):
        super(VariableRateLoan, self).__init__(term, rate, face, asset)
        self._rate_dict = rate_dict

    def rate(self, period):
        rate = self._rate_dict[min(self._rate_dict.keys())]
        rate_change_timestamps = sorted(self._rate_dict.keys())
        for next_rate_change_time in rate_change_timestamps:
            if period <= next_rate_change_time:
                break
            rate = self._rate_dict[next_rate_change_time]
        return rate


class AutoLoan(Loan):
    def __init__(self, term, rate, face, rate_dict, car):
        super(AutoLoan, self).__init__(term, rate, face, car)
        if not isinstance(car):
            print "car parameter must be car type"
            return
        self.car = car


if __name__ == '__main__':
    # Sanity checks
    # asset = Asset(0)
    # l = Loan(12, 0.01, 10000, asset)
    # for i in range(12):
    #     print l.interestDue(i), l.principalDue(i), l.balance(i)
    # vl = VariableRateLoan(12, 0.01, 10000, {0: 0.023, 5: 0.03, 10: 0.04}, asset)

    # 2.2.7f
    asset = Asset(20000)
    l = Loan(12, 0.01, 10000, asset)
    print l.equity(10)

    from asset import HouseBase
    house = HouseBase(100000)
    vl = FixedRateLoan(10, 0.01, 50000, house)
    print vl.recoveryValue(9)
