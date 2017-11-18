import loan
import asset
import csv


class LoanPool(object):
    def __init__(self, loan_list):
        self._l_list = loan_list

    def totalPrincipal(self):
        return sum(l.face for l in self._l_list)

    def totalBalance(self, period):
        return sum(l.balance(period) for l in self._l_list)

    def totalDues(self, period):
        principal_due = sum(l.principalDue(period) for l in self._l_list)
        interest_due = sum(l.interestDue(period) for l in self._l_list)
        payment_due = sum(l.monthlyPayment(period) for l in self._l_list)
        return principal_due, interest_due, payment_due

    def numOfActive(self, period):
        return len([l for l in self._l_list if l.balance(period) > 0])

    def getWaterfall(self, period):
        ret = []
        for l in self._l_list:
            ret.append([l.monthlyPayment(period), l.principalDue(period),
                        l.interestDue(period), l.balance(period)])
        return ret

    def loadCSV(self, file_path):
        with open(file_path, 'r') as fp:
            reader = csv.reader(fp, delimiter=',')
            header = next(reader, None)
            for row in reader:
                [loan_id, loan_type, face, rate, term, asset_type, asset_val] = row
                loan_type = ''.join(loan_type.strip().split(' '))
                face = float(face)
                rate = float(rate)
                term = int(term)
                asset_val = float(asset_val)
                asset_obj = getattr(asset, asset_type)(asset_val)
                loan_obj = getattr(loan, loan_type)(term, rate, face, asset_obj)
                self._l_list.append(loan_obj)

    def WAM(self):
        nominator = sum(l.face * l.rate for l in self._l_list)
        denominator = sum(l.rate for l in self._l_list)
        return nominator * 1.0 / denominator
