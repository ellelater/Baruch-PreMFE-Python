"""
This program demonstrates the use of built-in functions
"""


def get_mortgages():
    return [100, 200, 300, 400, 500, 600]


def minMortgages(morts):
    return [x for x in morts if x < 200]


def standardMortgages(morts):
    return [x for x in morts if 200 <= x <= 467]


def jumboMortgages(morts):
    return [x for x in morts if x > 467]


def main():
    # This is for 1.4.1 a
    mort_list = get_mortgages()

    # This is for 1.4.1 b
    min_morts = minMortgages(mort_list)
    std_morts = standardMortgages(mort_list)
    jmb_morts = jumboMortgages(mort_list)

    # This is for 1.4.1 c
    print 'All mortgage in minimum mortgages are below 200?'
    print all([x < 200 for x in min_morts])
    print 'All mortgage in standard mortgages are between 200 and 467?'
    print all([200 <= x <= 467 for x in std_morts])
    print 'All mortgage in jumbo mortgages are above 467?'
    print all([x > 467 for x in jmb_morts])

    # This is for 1.4.1 d
    print 'Any mortgage in minimum mortgages above 200?'
    print any([x >= 200 for x in min_morts])
    print 'Any mortgage in standard mortgages not between 200 and 467?'
    print any([x < 200 or x > 467 for x in std_morts])
    print 'Any mortgage in jumbo mortgages below 467?'
    print any([x <= 467 for x in jmb_morts])

    # This is for 1.4.2
    print 'Does the number of mortgages in all categories sum to the total number of mortgages?'
    print len(min_morts) + len(std_morts) + len(jmb_morts) == len(mort_list)

    # This is for 1.4.3
    print 'The total mortgage value:', sum(mort_list)

    # This is for 1.4.4
    print 'min/max for minimum mortgages:', min(min_morts), max(min_morts)
    print 'min/max for standard mortgages:', min(std_morts), max(std_morts)
    print 'min/max for jumbo mortgages:', min(jmb_morts), max(jmb_morts)

    # This is for 1.4.5
    print "What is the difference between the sum of jumbo mortgages and the sum of the others?"
    print abs(sum(min_morts + std_morts) - sum(jmb_morts))


if __name__ == '__main__':
    main()
