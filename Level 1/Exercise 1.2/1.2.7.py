"""
This program demonstrates the use of comprehensions.
"""


def main():
    lst = [i**2 for i in range(100)]

    # 7a list that contains only number above 1000
    lst_a = [i**2 for i in range(100) if i > 1000]

    # 7b list that contains only even numbers
    lst_b = [i**2 for i in range(100) if i % 2 == 0]


if __name__ == "__main__":
    main()