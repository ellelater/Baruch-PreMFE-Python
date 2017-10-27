import math


def main():
    hypotenuse = lambda h, b: math.sqrt(h**2 + b**2)
    for height, base in [(10, 5), (1., 1)]:
        print hypotenuse(height, base)


if __name__ == '__main__':
    main()