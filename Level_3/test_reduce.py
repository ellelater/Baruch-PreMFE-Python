def WAM(mort_list):
    denominator = sum(mort[0] for mort in mort_list)
    def fn(total, (face, term, rate)):
        return total + face * term * 1.0
    return reduce(fn, mort_list, 0) / denominator


mort_list = [(1000, 2, 0.1),
             (2000, 1, 0.2)]
print WAM(mort_list)

