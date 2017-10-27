def divide(nom, den):
    try:
        return 1. * nom / den
    except ZeroDivisionError as e:
        print e
    except TypeError as e:
        print e
        print "Wrong input type. Please try again."


def main():
    print divide(1, 0)
    print divide(0, '1')


if __name__ == '__main__':
    main()
