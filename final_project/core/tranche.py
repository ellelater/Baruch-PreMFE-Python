import logging


class Tranche(object):
    def __init__(self, notional, rate, sub_level):
        self.notional = notional
        self.rate = rate
        self.sub_level = sub_level


class StandardTranche(Tranche):
    def __init__(self, notional, rate, sub_level):
        super(StandardTranche, self).__init__(notional, rate, sub_level)
        self._cur_time = 0
        self._cur_ntl_balance = self.notional
        self._cur_prp_due = 0
        self._cur_int_due = 0
        self._int_shortfall = 0

        self._already_paid_int = False
        self._already_paid_prp = False

    def increaseTimePeriod(self):
        self._cur_time += 1
        self._already_paid_int = False
        self._already_paid_prp = False

    def makePrincipalPayment(self, amount):
        if self._already_paid_prp:
            logging.warn("Principal already paid at this time period!")
        else:
            # make payment
            self._already_paid_prp = True

    def makeInteresetPayment(self, amount):
        if self._already_paid_int:
            logging.warn("Interest already paid at this time period!")
        else:
            # make payment
            self._already_paid_int = True
        
    def notionalBalance(self):
        pass

    def interestDue(self):
        pass

    def reset(self):
        self._cur_time = 0
        self._cur_ntl_balance = self.notional
        self._cur_prp_due = 0
        self._cur_int_due = 0
        self._int_shortfall = 0



