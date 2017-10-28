from dependency.asset import Asset


class Loan(object):
    def __init__(self, term, rate, face, asset):
        if not isinstance(asset, Asset):
            print "asset parameter needs to be Asset type."
            return
        self._term = term
        self._rate = rate
        self._face = face
        self.asset = asset


def main():
    try:
        l = Loan(20, 0.02, 10000, "wrong asset")
    except TypeError as e:
        print e
    asset = Asset(20000)
    l = Loan(20, 0.02, 10000, asset)


if __name__ == '__main__':
    main()
