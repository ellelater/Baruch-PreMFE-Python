def WAM(amount_list, term_list):
    def fn(total, (face, term)):
        return total + face*term
    return reduce(fn, zip(amount_list, term_list), 0) / sum(amount_list)


def main():
    terms = [10, 20]
    rates = [0.2, 0.1]
    print WAM(rates, terms)


if __name__ == '__main__':
    main()