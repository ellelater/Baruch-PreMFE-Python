"""
This program demonstrate the use of '*args'
"""


def mean(*args):
    return sum(args) / len(args) * 1.0


if __name__ == '__main__':
    print mean(0, 1, 2, 3, 4)
    print mean(*range(5))
