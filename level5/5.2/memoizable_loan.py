'''
This program modifies the loan Class in Level 2 using exception handling.
'''
from asset import Asset
import logging
from memoizable import Memoizable


class MemoizableLoan(object):
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

    @Memoizable
    def interestDue(self, period):
        logging.warn("Using recursive version of waterfall algorithm.")
        if period <= 0 or period > self._term:
            logging.info("Period is negative or larger than term.")
            return 0
        return self.balance(period - 1) * self._rate

    @Memoizable
    def principalDue(self, period):
        logging.warn("Using recursive version of waterfall algorithm.")
        if period <= 0 or period > self._term:
            logging.info("Period is negative or larger than term.")
            return 0
        return self.monthlyPayment(period) - self.interestDue(period)

    @Memoizable
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
