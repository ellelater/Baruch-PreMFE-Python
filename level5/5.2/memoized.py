from functools import update_wrapper, partial


class Memoized(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}
        update_wrapper(self, func)

    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        else:
            ret = self.func(*args)
            self.cache[args] = ret
            return ret

    def __get__(self, obj, objtype):
        return partial(self.__call__, obj)


# below is for testing
@Memoized
def myFunc(x):
    print x


def main():
    myFunc(1)


if __name__ == '__main__':
    main()