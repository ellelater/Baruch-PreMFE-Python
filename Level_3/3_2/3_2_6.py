import itertools


def main():
    a = itertools.chain((i for i in xrange(10)),
                        (i for i in xrange(10, 15)),
                        (i for i in xrange(15, 20)))
    print list(a)


if __name__ == '__main__':
    main()
