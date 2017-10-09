"""
This program demonstrates the time cost of creating lists with for-loop and comprehension.
"""

import time


def main():
    # 10a creates the list with for-loop
    start1 = time.time()
    lst1 = []
    for i in range(10000000):
        if i % 10 == 0:
            lst1.append(i)
    print "Time cost of loop:", time.time() - start1  # 2.32 sec

    # 10b creates the list with comprehension
    start2 = time.time()
    lst2 = [i for i in range(10000000) if i % 10 == 0]
    print "Time cost of comprehension:", time.time() - start2  # 1.85 sec
    """
    The comprehension is a little faster than for-loop because
    the program looks up the list and does an append operation
    in each iteration, whereas in comprehension the construction
    is done more compactly.
    """

if __name__ == '__main__':
    main()
