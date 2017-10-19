import time


class Timer(object):
    def __init__(self, format):
        self._start = 0
        self._isrunning = False
        self._format = format
        self._last_time_taken = -1

    def start(self):
        if self._isrunning:
            raise RuntimeError('CURRENTLY RUNNING!!!')
        self._start = time.time()
        self._isrunning = True

    def end(self):
        if not self._isrunning:
            raise RuntimeError('HAS NOT STARTED!!!')
        time_taken = time.time() - self._start
        print 'Time taken:', self.convert_format(time_taken)
        self._isrunning = False
        self._last_time_taken = time_taken

    def convert_format(self, seconds):
        if self._format == 'hours':
            return seconds / 3600.
        if self._format == 'minutes':
            return seconds / 60.
        if self._format == 'seconds':
            return seconds

    def last_time_taken(self):
        if self._last_time_taken < 0:
            raise RuntimeError('NO LAST TIME RECORD AVAILABLE!!!')
        return self._last_time_taken


if __name__ == '__main__':
    T = Timer('hours')
    # basic functionality
    T.start()
    T.end()

    # Start error
    # T.start()
    # T.start()
    # End error
    # T.end()
    # T.end()

    # Format test
    T2 = Timer('minutes')
    T2.start()
    T2.end()
    T3 = Timer('seconds')
    T3.start()
    T3.end()

    # Last time taken test
    print T3.last_time_taken()
