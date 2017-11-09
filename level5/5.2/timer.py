'''
Modify Timer class to log errors instead of a print statement.
'''
import time
import logging
from functools import partial, update_wrapper


class Timer(object):
    warnThreshold = 60

    def __init__(self, func, warnThreshold=60):
        self._start = 0
        self._isrunning = False
        self._format = 'seconds'
        self._last_time_taken = -1
        self.warnThreshold = warnThreshold
        # decoration
        self.func = func
        update_wrapper(self, func)

    # Used for decorator
    def __call__(self, *args):
        self.start()
        ret = self.func(*args)
        self.end()
        return ret

    def __get__(self, obj, objtype):
        return partial(self.__call__, obj)

    def config_format(self, format):
        self._format = format

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end()

    def start(self):
        if self._isrunning:
            logging.info('Timer is currently running!')
        self._start = time.time()
        self._isrunning = True

    def end(self):
        if not self._isrunning:
            logging.info('Timer has not started!')
        time_taken = time.time() - self._start
        timer = self._convert_seconds(time_taken)
        print 'Time taken is {0:.5f}.'.format(timer)
        if timer > self.warnThreshold:
            logging.warning('Time taken {0} exceeds the warn threshold {1}!'.format(timer, self.warnThreshold))
        self._isrunning = False
        self._last_time_taken = time_taken

    def _convert_seconds(self, seconds):
        if self._format == 'seconds':
            return seconds
        if self._format == 'minutes':
            return seconds / 60
        if self._format == 'hours':
            return seconds / 3600


@Timer
def myFunc(x):
    print "X:", x


def main():
    logging.getLogger().setLevel(logging.INFO)
    myFunc(1)

if __name__ == '__main__':
    main()
