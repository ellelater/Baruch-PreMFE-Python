import time

def range_comp():
    a = [i**2 for i in range(5000000)]


def xrange_comp():
    a = [i ** 2 for i in xrange(5000000)]


def main():
    print "Range time cost:",
    start = time.time()
    range_comp()
    print time.time() - start

    print "Xrange time cost:",
    start = time.time()
    xrange_comp()
    print time.time() - start


if __name__ == '__main__':
    main()
