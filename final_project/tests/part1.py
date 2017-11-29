from core.loan_pool import LoanPool
from core.security import StructuredSecurities
from core.tranche import StandardTranche
from waterfall import doWaterfall
import utils
import itertools
import logging


def main():
    lp = LoanPool([])
    lp.loadCSV('../../Loans.csv')

    tr_percents = [0.8, 0.2]
    tr_rates = [0.1, 0.3]
    tr_levels = [0, 1]
    sc = utils.makeSecurities(lp.totalPrincipal(), tr_percents, tr_rates, tr_levels)

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
