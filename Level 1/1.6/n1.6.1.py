import math


def main():
    # use of trigonometrical functions
    print math.cos(0.4) ** 2 + math.sin(0.4) ** 2

    # use of logarithms
    print math.exp(math.log(5.))

    # use of arctan and pi
    print 4 * math.atan2(2., 2.) / math.pi

    # use of e and factorial
    print math.e / sum([1.0/math.factorial(n) for n in range(100)])

if __name__ == '__main__':
    main()
