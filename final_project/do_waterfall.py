from core.loan_pool import LoanPool
from core.security import StructuredSecurities


def doWaterfall(loan_pool, securities):
    assert isinstance(loan_pool, LoanPool) and isinstance(securities, StructuredSecurities),\
        "Invalid input type."
    period = 1
    lp_waterfalls = []
    sc_waterfalls = []
    reserve_cash = []
    while loan_pool.numOfActive(period) > 0:
        securities.increaseTimePeriod()
        sc_waterfalls.append(securities.getWaterfall())
        lp_waterfalls.append(loan_pool.getWaterfall(period))
        reserve_cash.append(securities.reserve_account)
        cash = loan_pool.totalDues(period)
        securities.makePayments(cash)
    return lp_waterfalls, sc_waterfalls, reserve_cash

