"""
This program demonstrates the use of double list comprehension.
"""


def main():
    # list of lists containing numbers 0~8
    lst = [[i + j for i in range(5)] for j in range(5)]
    # print lst


if __name__ == "__main__":
    main()