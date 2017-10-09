"""
This is a program that prints out the number and name of the days of the week.
"""


def main():
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    for number, name in zip(range(1, 8), days):
        print number, name


if __name__ == "__main__":
    main()
