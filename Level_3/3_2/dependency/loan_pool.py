from loan import Loan, FixedRateLoan, VariableRateLoan


class LoanPool(object):
    def __init__(self, loan_list):
        self._l_list = loan_list

    def totalPrincipal(self):
        return sum(l._face for l in self._l_list)

    def totalBalance(self, period):
        return sum(l.balance(period) for l in self._l_list)

    def totalDues(self, period):
        principal_due = sum(l.principalDue(period) for l in self._l_list)
        interest_due = sum(l.interestDue(period) for l in self._l_list)
        payment_due = sum(l.monthlyPayment(period) for l in self._l_list)
        return principal_due, interest_due, payment_due

    def numOfActive(self, period):
        return len([l for l in self._l_list if l.balance(period) > 0])

    def WAM(self):
        nominator = sum(l._face * l._rate for l in self._l_list)
        denominator = sum(l._rate for l in self._l_list)
        return nominator * 1.0 / denominator


if __name__ == "__main__":
    l1 = Loan(12, 0.01, 10000)
    l2 = FixedRateLoan(24, 0.08, 40000)
    lp = LoanPool([l1, l2])
    print lp.totalDues(5)
