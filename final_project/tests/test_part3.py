import logging

import utils
from core.loan_pool import LoanPool
from simulation.monte_carlos import simulateWaterfall, runMonte


def main():
    lp = LoanPool([])
    lp.loadCSV('Loans.csv')

    """ Testing simulateMonte """
    # tr_percents = [0.8, 0.2]
    # tr_rates = [0.1, 0.3]
    # tr_levels = [0, 1]
    # sc = utils.makeSecurities(lp.totalPrincipal(), tr_percents, tr_rates, tr_levels)
    # print simulateWaterfall(lp, sc, 2)

    """ Testing runMonte """
    rates = runMonte(lp, 1, 1e-3)
    print "Converged results:", rates


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    main()
