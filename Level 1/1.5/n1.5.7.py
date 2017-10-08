def get_morgages_dict():
    return {'asdfas': 100,
            'dioync': 199,
            'hniaud': 400,
            'asdfss': 500,
            'bytsds': 700}


def filter_min_mortgages(morts):
    return {k: v for k, v in morts.items() if v < 200}


def filter_std_mortgages(morts):
    return {k: v for k, v in morts.items() if 200 <= v <= 467}


def filter_jmb_mortgages(morts):
    return {k: v for k, v in morts.items() if v > 467}


def main():
    # 1.5.7 a
    mort_dict = get_morgages_dict()
    min_morts = filter_min_mortgages(mort_dict)
    std_morts = filter_std_mortgages(mort_dict)
    jmb_morts = filter_jmb_mortgages(mort_dict)
    print "Original mortgage dict:"
    print mort_dict

    # 1.5.7 b
    print "\n\n********** 1.5.7 b **********"
    print "Pre-modification minimum mortgages:"
    print min_morts

    min_morts['dioync'] = 0
    print "Post-modification minimum mortgages:"
    print min_morts
    print "Post-modification all mortgages:"
    print mort_dict
    """
    min_morts changed because its value is modified directly.
    mort_dict didn't change because min_morts is not linked to it, i.e.
    they are two independent objects.
    """

    # 1.5.7 c
    print "\n\n********** 1.5.7 c **********"
    min_mort_values = min_morts.values()
    print "Pre-modification minimum mortgages:"
    print min_morts

    min_mort_values[0] = -1
    print "Post-modification minimum mortgages:"
    print min_morts
    print "Post-modification all mortgages:"
    print mort_dict
    """
    min_morts didn't change because min_mort_values is not linked to it, i.e.
    the values in min_mort_values and min_morts are stored separately, thus 
    any modification on min_mort_values will not affect min_morts. 
    Similar for mort_dict.
    """


if __name__ == '__main__':
    main()