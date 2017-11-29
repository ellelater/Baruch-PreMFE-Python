import itertools
import logging

from core.loan_pool import LoanPool
from core.security import StructuredSecurities
from core.tranche import StandardTranche
from simulation.monte_carlos import simulateWaterfall
from waterfall import doWaterfall


def main():
    lp = LoanPool([])
    lp.loadCSV('../../Loans.csv')

    sc = StructuredSecurities(lp.totalPrincipal())
    # first tranche: 0.8 ntl per, 0.1 rate, sub_level 0
    sc.addTranche(StandardTranche, 0.8, 0.1, 0)
    # second tranche: 0.2 ntl per, 0.3 rate, sub_level 1
    sc.addTranche(StandardTranche, 0.2, 0.3, 1)

    print simulateWaterfall(lp, sc, 2)


if __name__ == '__main__':
    main()