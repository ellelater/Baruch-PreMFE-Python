def main():
    user_input = '1'
    loan_lst = []
    while user_input == '1':
        user_input = raw_input("Select one option: (1) Add a Loan; (2) Write file and exit.")
        if user_input != '1' and user_input != '2':
            print "Invalid option. Please re-type your input."
            continue
        if user_input == '1':
            ltype = raw_input("Type of Loan:")
            ltype = raw_input("Type of Loan:")