import itertools


def main():
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [7, 8, 9]

    for aa, bb, cc in itertools.product(a, b, c):
        print aa, bb, cc


if __name__ == '__main__':
    main()