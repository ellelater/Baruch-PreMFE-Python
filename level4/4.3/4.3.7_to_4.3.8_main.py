from loan import Loan
from asset import Asset


def process_input(avalue, lface, lrate, lterm):
    a = Asset(float(avalue))
    l = Loan(int(lterm), float(lrate), float(lface), a)
    return l


def war(lst):
    pass


def wam(lst):
    pass


def main():
    loan_lst = []
    while True:
        user_input = raw_input("Select one option:\n"
                               "(1) Add a Loan\n"
                               "(2) Write file and exit\n"
                               "(3) Load csv file\n"
                               "(4) Display the WAR and WAM of all loan.")
        if user_input not in ['1', '2', '3', '4']:
            print "Invalid option. Please re-type your input."
            continue
        if user_input == '1':
            ltype = raw_input("Type of Loan:")
            lface = raw_input("Face amount:")
            lrate = raw_input("Rate:")
            lterm = raw_input("Length of term:")
            aname = raw_input("Asset name:")
            avalue = raw_input("Asset value:")
            l = process_input(avalue, lface, lrate, lterm)
            loan_lst.append((ltype, aname, l))
            print "Loan has been recorded."
        elif user_input == '2':
            break
        elif user_input == '3':
            file_path = raw_input("Insert path for csv file:")
            with open(file_path, 'r') as f:
                for line in f:
                    ltype, aname, avalue, lface, lrate, lterm = line.strip().split(',')
                    l = process_input(avalue, lface, lrate, lterm)
                    loan_lst.append((ltype, aname, l))
            print "File has been loaded."
        else:
            print war(loan_lst)
            print wam(loan_lst)

    with open('loan_records.csv', 'w') as fp:
        for ltype, aname, loan in loan_lst:
            fp.write(','.join(map(str, [ltype, aname, loan.asset.val,
                                        loan._face, loan._rate, loan._term])) + '\n')


if __name__ == '__main__':
    main()
