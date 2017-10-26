def generator_fibon():
    first = 0
    second = 1
    while True:
        cur = first + second
        first, second = second, cur
        yield cur


if __name__ == '__main__':
    # first two
    for i, num in enumerate(generator_fibon()):
        if i > 1:
            break
        print num
    # next 100
    for i, num in enumerate(generator_fibon()):
        if i <= 1:
            continue
        if i > 100:
            break
        print num