from core.loan_pool import LoanPool
from core.security import StructuredSecurities
import logging
from utils import ABSRating


def doWaterfall(loan_pool, securities):
    assert isinstance(loan_pool, LoanPool) and isinstance(securities, StructuredSecurities),\
        "Invalid input type."
    period = 1
    lp_waterfalls = []
    sc_waterfalls = []
    reserve_cash = []
    while loan_pool.numOfActive(period) > 0:
        # print "Period {}, # of Loan left: {}".format(period, loan_pool.numOfActive(period))
        recovery = loan_pool.checkDefaults(period)  # get default recoveries
        cash = loan_pool.totalDues(period)[-1]  # get loan payments
        securities.makePayments(cash + recovery)  # pay securities
        sc_waterfalls.append(securities.getWaterfall())  # record waterfalls
        lp_waterfalls.append(loan_pool.getWaterfall(period))
        reserve_cash.append(securities.reserved_account)
        securities.increaseTimePeriod()  # new time period
        period += 1

    tr_payments = [[] for i in xrange(len(securities.tr_lst))]
    for period_wfs in sc_waterfalls:
        for tr_idx, tr_wf in enumerate(period_wfs):
            tr_payments[tr_idx].append(tr_wf[1] + tr_wf[3])  # get payments for each tranche
    tr_metrics = [(tr.IRR(payments), tr.DIRR(payments), tr.AL(payments), ABSRating(tr.DIRR(payments)))
                  for tr, payments in zip(securities.tr_lst, tr_payments)]  # get metrics
    return tr_metrics, lp_waterfalls, sc_waterfalls, reserve_cash
