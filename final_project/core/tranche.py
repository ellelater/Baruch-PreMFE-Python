'''
This program is for 7.1.1 and 7.1.2, creating a Tranche class and a StandardTranche class derived from it.
'''
import logging


class Tranche(object):
    def __init__(self, notional, notional_percent, rate, sub_level):
        self.notional = notional
        self.ntl_per = notional_percent
        self.rate = rate
        self.sub_level = sub_level


class StandardTranche(Tranche):
    def __init__(self, notional, notional_percent, rate, sub_level):
        super(StandardTranche, self).__init__(notional, notional_percent, rate, sub_level)
        self._cur_time = 0
        self._cur_ntl_balance = self.notional
        self._cur_int_due = 0
        self._int_shortfall = 0
        self._already_paid_int = False
        self._already_paid_prp = False

    def increaseTimePeriod(self):
        self._cur_time += 1
        self._cur_int_due = self.rate * self._cur_ntl_balance + self._int_shortfall
        self._int_shortfall = 0
        self._already_paid_int = False
        self._already_paid_prp = False

    def makePrincipalPayment(self, amount):
        if self._already_paid_prp:
            logging.warn("Principal already paid at this time period!")
        elif self._cur_ntl_balance == 0:
            logging.warn("Current notional balance is 0. Payment not accepted!")
        else:  # make the payment
            self._already_paid_prp = True
            if self._cur_ntl_balance > amount:
                self._cur_ntl_balance -= amount
                amount = 0
            else:  # prepayment
                amount -= self._cur_ntl_balance
                self._cur_ntl_balance = 0
        return amount

    def makeInterestPayment(self, amount):
        if self._already_paid_int:
            logging.warn("Interest already paid at this time period!")
        elif self._cur_int_due == 0:
            logging.warn("Current interest due is 0. Payment not accepted!")
        else:  # make the payment
            self._already_paid_int = True
            if self._cur_int_due > amount:
                self._cur_int_due -= amount
                self._int_shortfall = self._cur_int_due
                amount = 0
            else:
                amount -= self._cur_int_due
                self._cur_int_due = 0
        return amount

    def notionalBalance(self):
        return self._cur_ntl_balance

    def interestDue(self):
        return self._cur_int_due

    def reset(self):
        self._cur_time = 0
        self._cur_ntl_balance = self.notional
        self._cur_int_due = 0
        self._int_shortfall = 0
        self._already_paid_int = False
        self._already_paid_prp = False
