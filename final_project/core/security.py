from tranche import *


class StructuredSecurity(object):
    def __init__(self, notional):
        self.tr_lst = []
        self.ttl_ntl = notional
        self.mode = "Sequential"
        self.reserved_account = 0

    def addTranche(self, cls, ntl_per, rate, sub_level):
        assert issubclass(cls, Tranche), "Input class type must be a tranche."
        new_tr = cls(ntl_per, rate, sub_level)
        self.tr_lst.append(new_tr)

    def change_mode(self, mode):
        self.mode = mode

    def increaseTimePeriod(self):
        for tr in self.tr_lst:
            tr.increaseTimePeriod()

    def makePayments(self, cash_amount):
        # Calculate each payments and pay according to self.mode
        for tr in self.tr_lst:
            tr.makePrincipalPayment(0)
            tr.makeInterestPayment(0)

        # deal with left over cash here

    def getWaterfall(self):
        ret = [[] for tr in self.tr_lst]
        for i, tr in enumerate(self.tr_lst):
            # Calculate these quantities for each tranche
            int_due = 0
            int_paid = 0
            int_shortfall = 0
            prp_paid = 0
            balance = 0
            ret[i] = [int_due, int_paid, int_shortfall, prp_paid, balance]
        return ret