from asset import Asset, Car
import logging


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

    def monthlyPayment(self, period):  # period is a dummy parameter
        return self._pmt_per_month

    def totalPayments(self):
        return sum([self.monthlyPayment(period) for period in range(self._term)])

    def totalInterest(self):
        return self.totalPayments() - self._face

    def interestDue(self, period):
        logging.warn("Using recursive version of waterfall algorithm.")
        if period <= 0 or period > self._term:
            logging.info("Period is negative or larger than term.")
            return 0
        return self.balance(period - 1) * self._rate

    def principalDue(self, period):
        logging.warn("Using recursive version of waterfall algorithm.")
        if period <= 0 or period > self._term:
            logging.info("Period is negative or larger than term.")
            return 0
        return self.monthlyPayment(period) - self.interestDue(period)

    def balance(self, period):
        logging.warn("Using recursive version of waterfall algorithm.")
        if period <= 0 or period > self._term:
            logging.info("Period is negative or larger than term.")
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

    def rate(self, period):
        # This shows how to find the rate for certain period in a rateDict
        rate = self._rateDict[min(self._rateDict.keys())]
        rate_change_timestamps = sorted(self._rateDict.keys())
        for next_rate_change_time in rate_change_timestamps:
            if period <= next_rate_change_time:
                break
            rate = self._rateDict[next_rate_change_time]
        return rate


class AutoLoan(Loan):
    def __init__(self, term, rate, face, rateDict, car):
        super(AutoLoan, self).__init__(term, rate, face, car)
        if not isinstance(car, Car):
            logging.error("Input must be a Car type.")
            return
        self.car = car
