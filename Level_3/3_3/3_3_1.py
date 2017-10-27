def divide(nom, den):
    try:
        return 1. * nom / den
    except ZeroDivisionError as e:
        print e


def main():
    print divide(1, 0)


if __name__ == '__main__':
    main()
