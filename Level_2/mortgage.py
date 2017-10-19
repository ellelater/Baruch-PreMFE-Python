from loan import Loan, FixedRateLoan, VariableRateLoan


class MortgageMixin(object):
    def __init__(self):
        self._ltv = 1.0

    def pmi(self):
        return self._face * 0.000075 if self._ltv > 0.8 else 0

    def monthlyPayment(self, period):
        return super(MortgageMixin, self).monthlyPayment(period) + self.pmi()

    # Actually no need to override principalDue
    def principalDue(self, period):
        return self.monthlyPayment(period) - self.interestDue(period)


class VariableMortgage(MortgageMixin, VariableRateLoan):
    def __init__(self, asset_val, term, rate, face, rate_dict):
        super(VariableMortgage, self).__init__()
        VariableRateLoan.__init__(self, term, rate, face, rate_dict)


class FixedRateMortgage(MortgageMixin, FixedRateLoan):
    def __init__(self, asset_val, term, rate, face):
        super(FixedRateMortgage, self).__init__()
        FixedRateLoan.__init__(self, term, rate, face)


if __name__ == '__main__':
    vm = VariableMortgage(10000, 12, 0.01, 10000, {0: 0.023, 5: 0.03, 10: 0.04})
    print vm.pmi()
    print vm.rate(4.4)
