from tranche import *


class StructuredSecurities(object):
    def __init__(self, notional):
        self.tr_lst = []
        self.ttl_ntl = notional
        self.mode = "Sequential"
        self.reserved_account = 0

    def addTranche(self, cls, ntl_per, rate, sub_level):
        assert issubclass(cls, Tranche), "Input class type must be a tranche."
        new_tr = cls(ntl_per * self.ttl_ntl, ntl_per, rate, sub_level)
        self.tr_lst.append(new_tr)
        self.tr_lst = sorted(self.tr_lst, key=lambda x: x.sub_level)

    def totalInterestDue(self):
        return sum(tr.interestDue() for tr in self.tr_lst)

    def change_mode(self, mode):
        assert mode in {'Sequential', 'Pro Rata'}, "Invalid mode."
        self.mode = mode

    def increaseTimePeriod(self):
        for tr in self.tr_lst:
            tr.increaseTimePeriod()

    def makePayments(self, cash_amount):
        cash_left = cash_amount + self.reserved_account
        for tr in self.tr_lst:
            if tr.notionalBalance > 0:
                cash_left = tr.makeInterestPayment(cash_left)
        if cash_left > 0:  # deal with cash left over here
            if self.mode == "Sequential":
                for tr in self.tr_lst:
                    if tr.notionalBalance > 0 and cash_left > 0:
                        cash_left = tr.makePrincipalPayment(cash_left)
            elif self.mode == 'Pro Rata':
                tmp_cash_left = 0
                for tr in self.tr_lst:
                    if tr.notionalBalance > 0:
                        tmp_cash_left += tr.makePrincipalPayment(tr.ntl_per * cash_left)
                cash_left = tmp_cash_left
        self.reserved_account += cash_left

    def getWaterfall(self):
        ret = [[] for tr in self.tr_lst]
        for i, tr in enumerate(self.tr_lst):
            # Calculate these quantities for each tranche
            int_due = tr.interestDue
            int_paid = tr.interestPaid
            int_shortfall = tr.interestShortfall
            prp_paid = tr.principalPaid
            balance = tr.notionalBalance
            ret[i] = [int_due, int_paid, int_shortfall, prp_paid, balance]
        return ret

    def reset(self):
        for tr in self.tr_lst:
            tr.reset()
