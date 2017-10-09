"""
This is a program that prints out Fibonacci sequence
"""


def iterative_fibonacci(N):
    """
    Return Fibonacci sequence up to N using iteration
    :param N:
    :return:
    """
    ret = []
    second_last = 1
    last = 0
    while (second_last + last) < N:
        current = second_last + last
        ret.append(current)
        second_last = last
        last = current
    return ret


def recursion(N, second_last, last, ret):
    """
    Actual recursion function
    :param N:
    :param second_last: second last element of the current sequence
    :param last: last element of the current sequence
    :param ret: current sequence, starting from 1
    :return:
    """
    current = second_last + last
    if current < N:
        ret.append(current)
        return recursion(N, last, current, ret)
    else:
        return ret


def recursive_fibonacci(N):
    """
    Return Fibonacci sequence up to N using recursion
    :param N:
    :return:
    """
    return recursion(N, 1, 0, [])


if __name__ == "__main__":
    print iterative_fibonacci(10)
    print recursive_fibonacci(10)
