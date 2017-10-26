from dependency.loan import Loan
from dependency.asset import Asset


class LoanPool(object):
    def __init__(self, loan_list):
        self._l_list = loan_list

    # 3.2.3
    def __iter__(self):
        return iter(self._l_list)


if __name__ == "__main__":
    dummy_asset = Asset(1000)
    l1 = Loan(12, 0.01, 10000, dummy_asset)
    l2 = Loan(10, 0.1, 20000, dummy_asset)
    lp = LoanPool([l1, l2])
    for l in lp:
        print l._face
