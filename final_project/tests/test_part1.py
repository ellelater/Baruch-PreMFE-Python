from final_project.core.loan_pool import LoanPool
from final_project.core.security import StructuredSecurities
from final_project.core.tranche import StandardTranche
from final_project.do_waterfall import doWaterfall
import itertools


def main():
    lp = LoanPool([])
    lp.loadCSV('../../Loans.csv')
    print lp.totalPrincipal()
    for t in range(20, 50):
        print lp.totalBalance(t)
    for lwf in lp.getWaterfall(5)[:10]:
        print lwf

    sc = StructuredSecurities(lp.totalPrincipal())
    # first tranche: 0.8 ntl per, 0.1 rate, sub_level 0
    sc.addTranche(StandardTranche, 0.8, 0.1, 0)
    # second tranche: 0.2 ntl per, 0.2 rate, sub_level 1
    sc.addTranche(StandardTranche, 0.8, 0.1, 0)

    # What is "some clever list comprehension"?
    lp_wf, sc_wf, res_amounts = doWaterfall(lp, sc)
    with open('loan_pool_waterfall.csv', 'w') as lp:
        for loans in lp_wf:
            lp.write(','.join(map(str, list(itertools.chain(loans)))) + '\n')

    with open('securities_waterfall.csv', 'w') as sc:
        for tranches, res_cash in zip(sc, res_amounts):
            sc.write(','.join(map(str, list(itertools.chain(tranches))) +
                              [str(res_cash)]) + '\n')

if __name__ == '__main__':
    main()
