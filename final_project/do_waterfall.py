from core.loan_pool import LoanPool
from core.security import StructuredSecurities
import logging


def doWaterfall(loan_pool, securities):
    assert isinstance(loan_pool, LoanPool) and isinstance(securities, StructuredSecurities),\
        "Invalid input type."
    period = 1
    lp_waterfalls = []
    sc_waterfalls = []
    reserve_cash = []
    while loan_pool.numOfActive(period) > 0:
        logging.info("Period {}, # of Loan left: {}".format(period, loan_pool.numOfActive(period)))
        cash = loan_pool.totalDues(period)[-1]
        securities.makePayments(cash)
        sc_waterfalls.append(securities.getWaterfall())
        lp_waterfalls.append(loan_pool.getWaterfall(period))
        reserve_cash.append(securities.reserved_account)
        securities.increaseTimePeriod()
        period += 1
    return lp_waterfalls, sc_waterfalls, reserve_cash
