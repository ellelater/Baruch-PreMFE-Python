from timer import Timer
from asset import Asset
from loan import Loan
from memoizable_loan import MemoizableLoan
import logging

logging.basicConfig(level=logging.ERROR)

def main():
    a = Asset(1000)
    normal_loan = Loan(12, 0.3, 1000, a)
    memoizable_loan = MemoizableLoan(12, 0.3, 1000, a)

    print "Normal loan time cost:"
    with Timer():
        normal_loan.interestDue(10)

    print "Memoizable loan time cost:"
    with Timer():
        memoizable_loan.interestDue(10)


if __name__ == '__main__':
    main()