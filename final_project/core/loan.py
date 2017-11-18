from asset import Asset
import logging
from final_project.utils import Memoized


class Loan(object):
    def __init__(self, term, rate, face, asset):
        if not isinstance(asset, Asset):
            logging.error("Input must be of asset class")
            raise TypeError('input must be of asset class')
        self._term = term
        self._rate = rate
        self._face = face
        self.asset = asset
        self._pmt_per_month = self._rate * self._face / (1 - (1 + self._rate)**(-self._term))

    @property
    def term(self):
        return self._term

    @property
    def face(self):
        return self._face

    @property
    def rate(self, period=0):
        return self._rate

    def monthlyPayment(self, period):  # period is a dummy parameter
        return self._pmt_per_month

    def totalPayments(self):
        return sum([self.monthlyPayment(period) for period in range(self._term)])

    def totalInterest(self):
        return self.totalPayments() - self._face

    @Memoized
    def interestDue(self, period):
        if period <= 0 or period > self._term:
            logging.warn("Invalid period")
            return 0
        return self.balance(period - 1) * self._rate

    @Memoized
    def principalDue(self, period):
        if period <= 0 or period > self._term:
            logging.warn("Invalid period")
            return 0
        return self.monthlyPayment(period) - self.interestDue(period)

    @Memoized
    def balance(self, period):
        if period == 0:
            return self.face
        if period < 0 or period > self._term:
            logging.warn("Invalid period")
            return 0
        return self._face * (1 + self._rate) ** period - self.monthlyPayment(period) * \
                                                         ((1 + self._rate) ** period - 1) / self._rate

    def recoveryValue(self, period):
        return self.asset.current_val(period) * 0.6  # recovery multiplier

    def equity(self, period):
        return self.asset.current_val(period) - self.balance(period)


class FixedRateLoan(Loan):
    def __init__(self, term, rate, face, asset):
        super(FixedRateLoan, self).__init__(term, rate, face, asset)


class VariableRateLoan(Loan):
    def __init__(self, term, rate, face, rateDict, asset):
        super(VariableRateLoan, self).__init__(term, rate, face, asset)
        self._rateDict = rateDict

    def rate(self, period=0):
        # This shows how to find the rate for certain period in a rateDict
        rate = self._rateDict[min(self._rateDict.keys())]
        rate_change_timestamps = sorted(self._rateDict.keys())
        for next_rate_change_time in rate_change_timestamps:
            if period <= next_rate_change_time:
                break
            rate = self._rateDict[next_rate_change_time]
        return rate


class LoanPool(object):
    def __init__(self, loan_list):
        self._l_list = loan_list

    def totalPrincipal(self):
        return sum(l.face for l in self._l_list)

    def totalBalance(self, period):
        return sum(l.balance(period) for l in self._l_list)

    def totalDues(self, period):
        principal_due = sum(l.principalDue(period) for l in self._l_list)
        interest_due = sum(l.interestDue(period) for l in self._l_list)
        payment_due = sum(l.monthlyPayment(period) for l in self._l_list)
        return principal_due, interest_due, payment_due

    def numOfActive(self, period):
        return len([l for l in self._l_list if l.balance(period) > 0])

    def getWaterfall(self, period):
        ret = []
        for l in self._l_list:
            ret.append([l.monthlyPayment(period), l.principalDue(period),
                        l.interestDue(period), l.balance(period)])
        return ret

    def WAM(self):
        nominator = sum(l.face * l.rate for l in self._l_list)
        denominator = sum(l.rate for l in self._l_list)
        return nominator * 1.0 / denominator
