from core.loan_pool import LoanPool
from core.security import StructuredSecurities
from core.tranche import StandardTranche
from waterfall import doWaterfall
import itertools
import logging


def main():
    lp = LoanPool([])
    lp.loadCSV('../../Loans.csv')

    sc = StructuredSecurities(lp.totalPrincipal())
    # first tranche: 0.8 ntl per, 0.1 rate, sub_level 0
    sc.addTranche(StandardTranche, 0.8, 0.1, 0)
    # second tranche: 0.2 ntl per, 0.3 rate, sub_level 1
    sc.addTranche(StandardTranche, 0.2, 0.3, 1)

    # TODO: What is "some clever list comprehension"?
    # Printing results
    tr_metrics, lp_wf, sc_wf, res_amounts = doWaterfall(lp, sc)
    print "IRR\tDIRR\tAL\tLetterRating"
    for tr_metric in tr_metrics:
        print "{}\t{}\t{}\t{}".format(*tr_metric)
    # Saving csvs
    with open('loan_pool_waterfall.csv', 'w') as lp_fp:
        for loans in lp_wf:
            lp_fp.write(','.join(map(str, list(itertools.chain(loans)))) + '\n')

    with open('securities_waterfall.csv', 'w') as sc_fp:
        for tranches, res_cash in zip(sc_wf, res_amounts):
            sc_fp.write(','.join(map(str, list(itertools.chain(tranches))) +
                                 [str(res_cash)]) + '\n')


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
    main()
