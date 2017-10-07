"""
This program calculates the mean of a list
"""


# This is for 1.3.3
def mean(list):
    return sum(list) / len(list) * 1.0


# This is for 1.3.4
def variance(list):
    N = len(list)
    sqsum = 0
    m = mean(list)
    for x in list:
        sqsum += (x - m)**2
    return sqsum / N


# This is for 1.3.5
def variance_with_option(list, degOfFreedom=1):
    if degOfFreedom != 0 and degOfFreedom != 1:
        print "Wrong degree of freedom!"
        return None
    N = len(list)
    sqsum = 0
    m = mean(list)
    for x in list:
        sqsum += (x - m) ** 2
    return sqsum / (N - degOfFreedom)


if __name__ == "__main__":
    test_list = range(5)
    print mean(test_list)
    print variance(test_list)
    print variance_with_option(test_list)
    print variance_with_option(test_list, degOfFreedom=0)
