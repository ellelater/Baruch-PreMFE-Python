'''
This program is for 7.1.1 and 7.1.2, creating a Tranche class and a StandardTranche class derived from it.
'''
import logging
import numpy as np


class Tranche(object):
    def __init__(self, notional, notional_percent, rate, sub_level):
        self.notional = notional
        self.ntl_per = notional_percent
        self.rate = rate
        self.sub_level = sub_level

    def IRR(self, payments):
        return np.irr([-self.notional] + payments) * 12

    def DIRR(self, payments):
        return self.IRR(payments) - self.rate

    def AL(self, payments):
        return sum((i+1)*payments[i] for i in xrange(len(payments))) / self.notional


# TODO: Pay 0 equals to hasnt paid?
class StandardTranche(Tranche):
    def __init__(self, notional, notional_percent, rate, sub_level):
        super(StandardTranche, self).__init__(notional, notional_percent, rate, sub_level)
        self._cur_time = 0
        self._cur_ntl_balance = self.notional
        self._cur_int_due = 0
        self._cur_int_shortfall = 0
        self._cur_int_paid = 0
        self._cur_prp_paid = 0

    @property
    def notionalBalance(self):
        return self._cur_ntl_balance

    @property
    def interestDue(self):
        return self._cur_int_due

    @property
    def interestPaid(self):
        return self._cur_int_paid

    @property
    def principalPaid(self):
        return self._cur_prp_paid

    @property
    def interestShortfall(self):
        return self._cur_int_shortfall

    def increaseTimePeriod(self):
        self._cur_time += 1
        self._cur_int_due = self.rate * self._cur_ntl_balance + self._cur_int_shortfall
        self._cur_int_shortfall = 0
        self._cur_int_paid = 0
        self._cur_prp_paid = 0

    def makePrincipalPayment(self, amount):
        if self._cur_prp_paid > 0:
            logging.warn("Principal already paid at this time period!")
        elif self._cur_ntl_balance == 0:
            logging.warn("Current notional balance is 0. Payment not accepted!")
        else:  # make the payment
            self._cur_prp_paid = min(self._cur_ntl_balance, amount)
            self._cur_ntl_balance -= self._cur_prp_paid
        return amount - self._cur_prp_paid  # return cash left after payment

    def makeInterestPayment(self, amount):
        if self._cur_int_paid > 0:
            logging.warn("Interest already paid at this time period!")
        elif self._cur_int_due == 0:
            logging.warn("Current interest due is 0. Payment not accepted!")
        else:  # make the payment
            self._cur_int_paid = min(self._cur_int_due, amount)
            self._cur_int_shortfall = self._cur_int_due - self._cur_int_paid  # record shortfall
        return amount - self._cur_int_paid

    def reset(self):
        self._cur_time = 0
        self._cur_ntl_balance = self.notional
        self._cur_int_due = 0
        self._cur_int_shortfall = 0
        self._cur_int_paid = 0
        self._cur_prp_paid = 0
