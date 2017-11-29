from final_project.core.loan_pool import LoanPool


def main():
    lp = LoanPool([])
    lp.loadCSV('../../Loans.csv')
    print lp.totalPrincipal()
    for t in range(20, 50):
        print lp.totalBalance(t)
    for lwf in lp.getWaterfall(5)[:10]:
        print lwf


if __name__ == '__main__':
    main()
