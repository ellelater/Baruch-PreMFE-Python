from asset import Asset, Car
import logging
from utils import Memoized


class Loan(object):
    """
    Loan Base class
    """
    def __init__(self, term, rate, face, asset):
        if not isinstance(asset, Asset):
            logging.error("Input must be of asset class")
            raise TypeError('input must be of asset class')
        self._term = term
        self._rate = rate
        self._face = face
        self.asset = asset
        self._pmt_per_month = self._rate * self._face / (1 - (1 + self._rate)**(-self._term))
        self.defaulted = False

    @property
    def term(self):
        return self._term

    @property
    def face(self):
        return 0 if self.defaulted else self._face

    @property
    def rate(self, period=0):
        return self._rate

    def monthlyPayment(self, period):  # period is a dummy parameter
        return 0 if self.defaulted else self._pmt_per_month

    def totalPayments(self):
        return sum([self.monthlyPayment(period) for period in range(self._term)])

    def totalInterest(self):
        return self.totalPayments() - self._face

    @Memoized
    def interestDue(self, period):
        if period <= 0:
            logging.warn("Invalid period")
            return 0
        elif period > self._term:
            logging.info("Loan expired")
            return 0
        return self.balance(period - 1) * self._rate

    @Memoized
    def principalDue(self, period):
        if period <= 0:
            logging.warn("Invalid period")
            return 0
        elif period > self._term:
            logging.info("Loan expired")
            return 0
        return self.monthlyPayment(period) - self.interestDue(period)

    @Memoized
    def balance(self, period):
        if period == 0:
            return self.face
        if period < 0:
            logging.warn("Invalid period")
            return 0
        elif period > self._term:
            logging.info("Loan expired")
            return 0
        elif self.defaulted:
            logging.info("Loan defaulted")
            return 0
        return self.face * (1 + self.rate) ** period - self.monthlyPayment(period) * \
                                                       ((1 + self.rate) ** period - 1) / self.rate

    def checkDefault(self, flag):
        if flag == 0:
            self.defaulted = True
        """ I chose to not set the face and balance value to 0, but instead return 0 when they are called,
            which appears the same from outside of the Loan class. (See self.face and self.balance)
            This is for the sake of reset function. If they are directly set to 0 after being defaulted, they
            cannot be recovered for the next simulation and the object needs to be reconstructed from csv. 
        """

    def reset(self):
        self.defaulted = False

    def recoveryValue(self, period):
        return self.asset.current_val(period) * 0.6  # recovery multiplier

    def equity(self, period):
        return self.asset.current_val(period) - self.balance(period)


class FixedRateLoan(Loan):
    def __init__(self, term, rate, face, asset):
        super(FixedRateLoan, self).__init__(term, rate, face, asset)


class AutoLoan(Loan):
    def __init__(self, term, rate, face, car):
        super(AutoLoan, self).__init__(term, rate, face, car)
        if not isinstance(car, Car):
            logging.error("Input must be a Car type.")
            return
        self.car = car

