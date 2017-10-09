def mode(occurrences):
    frequency = {}
    for o in occurrences:
        if o in frequency:
            frequency[o] += 1
        else:
            frequency[o] = 1
    return frequency.items()


def main():
    tests = [[],
             [0, 0, 1],
             [0, '0', 1 - 1, '1-1'],
             [0, None]]
    for test in tests:
        print mode(test)


if __name__ == '__main__':
    main()
