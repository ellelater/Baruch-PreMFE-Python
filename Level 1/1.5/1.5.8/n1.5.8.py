def get_morgages_dict():
    return {'asdfas': (100000, 0.02, 12),
            'dioync': (400000, 0.01, 24),
            'hniaud': (1000000, 0.02, 12),
            'asdfss': (300000, 0.015, 12),
            'bytsds': (500000, 0.015, 6)}


def weighted_average_rate(mort_list):
    nominator = 0
    denominator = 0
    for amount, rate, term in mort_list:
        nominator += amount * rate * 1.0
        denominator += amount
    return nominator / denominator


def weighted_average_maturity(mort_list):
    nominator = 0
    denominator = 0
    for amount, rate, term in mort_list:
        nominator += amount * term * 1.0
        denominator += amount
    return nominator / denominator


def main():
    # 1.5.8 a
    mort_dict = get_morgages_dict()
    mort_list = sorted(mort_dict.values(), key=lambda (amount, rate, term): amount, reverse=True)
    # print mort_list

    # 1.5.8 b
    print weighted_average_rate(mort_list)

    # 1.5.8 c
    print weighted_average_maturity(mort_list)

    # 1.5.8 d
    term_dict = {}
    for key, value in mort_dict.items():
        amount, rate, term = value
        if term in term_dict:
            term_dict[term].append((amount, rate))
        else:
            term_dict[term] = [(amount, rate)]
            # print term_dict


if __name__ == '__main__':
    main()
