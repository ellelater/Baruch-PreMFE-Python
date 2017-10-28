import time


class Timer(object):
    def __init__(self):
        self._start = 0
        self._isrunning = False
        self._format = 'seconds'
        self._last_time_taken = -1

    def config_format(self, format):
        self._format = format

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end()

    def start(self):
        if self._isrunning:
            raise RuntimeError('CURRENTLY RUNNING!!!')
        self._start = time.time()
        self._isrunning = True

    def end(self):
        if not self._isrunning:
            raise RuntimeError('HAS NOT STARTED!!!')
        time_taken = time.time() - self._start
        print 'Time taken:', self._convert_seconds(time_taken)
        self._isrunning = False
        self._last_time_taken = time_taken

    def _convert_seconds(self, seconds):
        if self._format == 'seconds':
            return seconds
        if self._format == 'minutes':
            return seconds / 60
        if self._format == 'hours':
            return seconds / 3600


if __name__ == '__main__':
    with Timer() as t:
        t.config_format('seconds')
        print "Do something..."
