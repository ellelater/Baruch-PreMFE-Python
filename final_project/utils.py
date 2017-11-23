import time
import logging
from functools import partial, update_wrapper
import numpy as np


ABSRatingRates = np.array([-1, 0.06, 0.67, 1.3, 2.7, 5.2, 8.9, 13, 19, 27, 46, 72, 106, 143, 183, 231, 311, 2500, 10000])
ABSRatingLetters = ["Aaa", "Aa1", "Aa2", "Aa3", "A1", "A2", "A3",
                    "Baa1", "Baa2", "Baa3", "Ba1", "Ba2", "Ba3", "B1", "B2", "B3", "Caa", "Ca"]


def ABSRating(dirr):
    idx = np.where(ABSRatingRates >= dirr/100.)[0][0] - 1
    return ABSRatingLetters[idx]


class Timer(object):
    warnThreshold = 60

    def __init__(self, warnThreshold=60):
        self._start = 0
        self._isrunning = False
        self._format = 'seconds'
        self._last_time_taken = -1
        self.warnThreshold = warnThreshold

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
