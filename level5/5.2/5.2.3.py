from timer import Timer
from asset import Asset
from loan import Loan
from memoized_loan import MemoizedLoan
import logging

logging.basicConfig(level=logging.ERROR)


def main():
    a = Asset(1000)
    normal_loan = Loan(12, 0.3, 1000, a)
    memoizable_loan = MemoizedLoan(12, 0.3, 1000, a)

    print "First normal loan time cost:"
    normal_loan.interestDue(10)
    print "Second normal loan time cost:"
    normal_loan.interestDue(10)

    print "First memoizable loan time cost:"
    memoizable_loan.interestDue(10)
    print "Second memoizable loan time cost:"
    memoizable_loan.interestDue(10)


if __name__ == '__main__':
    main()
