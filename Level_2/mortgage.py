from loan import Loan, FixedRateLoan, VariableRateLoan
from asset import HouseBase


class MortgageMixin(object):
    def __init__(self, home):
        if not isinstance(home, HouseBase):
            print "home parameter needs to be HouseBase type."
            return
        self.home = home
        self._ltv = self._face * 1.0 / self.home.val

    def pmi(self):
        return self._face * 0.000075 if self._ltv > 0.8 else 0

    def realtime_pmi(self, period):
        paid_principal = sum(self.principalDue(t) for t in range(period))
        ltv = (self._face - paid_principal) / self.asset.val
        return self._face * 0.000075 if ltv > 0.8 else 0

    def monthlyPayment(self, period):
        return super(MortgageMixin, self).monthlyPayment(period) + self.pmi()

    # Actually no need to override principalDue
    def principalDue(self, period):
        return self.monthlyPayment(period) - self.interestDue(period)


class VariableMortgage(MortgageMixin, VariableRateLoan):
    def __init__(self, term, rate, face, rate_dict, home):
        VariableRateLoan.__init__(self, term, rate, face, rate_dict, home)
        super(VariableMortgage, self).__init__(home)


class FixedRateMortgage(MortgageMixin, FixedRateLoan):
    def __init__(self, term, rate, face, home):
        FixedRateLoan.__init__(self, term, rate, face, home)
        super(FixedRateMortgage, self).__init__(home)


if __name__ == '__main__':
    house = HouseBase(11000)
    vm = VariableMortgage(12, 0.01, 10000, {0: 0.023, 5: 0.03, 10: 0.04}, house)
    print vm.realtime_pmi(1)
    print vm.pmi()
    print vm.rate(4.4)
