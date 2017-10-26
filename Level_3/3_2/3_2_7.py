def main():
    a = zip((i for i in xrange(10)),
            (i for i in xrange(10, 20)),
            (i for i in xrange(20, 30)))
    print list(a)


if __name__ == '__main__':
    main()
