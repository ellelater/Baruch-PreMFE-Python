class Memoizable(object):
    def __init__(self, func):
        print "init", func.__dict__
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        print "Memoize", args
        if args in self.cache:
            return self.cache[args]
        else:
            ret = self.func(*args)
            self.cache[args] = ret
            return ret