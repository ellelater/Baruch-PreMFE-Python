def fact(n):
    ret = 1
    try:
        for i in xrange(n+1):
            ret *= i
        return ret
    except TypeError as e:
        print e
        print "Wrong input type"


def main():
    print fact(1.)
    print fact('2')
    print fact(0)


if __name__ == '__main__':
    main()
