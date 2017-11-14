import multiprocessing
import time
import logging
from monty_hall.game import MontyHallGame
from monty_hall.player import RandomPlayer


def MC(num_trial):
    g = MontyHallGame()
    p = RandomPlayer('Elle')

    switch_result = [0., 0]
    noswitch_result = [0., 0]
    for trial in xrange(num_trial):
        result = g.play(p)
        if p.switched:
            switch_result[1] += 1
            switch_result[0] += result
        else:
            noswitch_result[1] += 1
            noswitch_result[0] += result
    switch_rate = switch_result[0] / switch_result[1]
    noswitch_rate = noswitch_result[0] / noswitch_result[1]
    return switch_rate, noswitch_rate


def doWork(iptq, optq):
    while True:
        try:
            f, args = iptq.get(timeout=0.1)
            ret = f(*args)
            optq.put(ret)
        except:
            optq.put("Done")
            break


def main(num_trial, num_proc):
    logging.basicConfig(level=logging.ERROR)
    inpq = multiprocessing.Queue()
    resq = multiprocessing.Queue()
    for i in xrange(num_proc):
        inpq.put((MC, (num_trial/num_proc,)))
    procs = [multiprocessing.Process(target=doWork, args=(inpq, resq)) for i in xrange(num_proc)]
    switch_rate = 0
    noswitch_rate = 0

    start = time.time()
    for p in procs:
        p.start()
    while True:
        res = resq.get()
        if res == "Done":
            break
        else:
            switch_rate += res[0]
            noswitch_rate += res[1]
    time_taken = time.time() - start

    switch_rate /= num_proc
    noswitch_rate /= num_proc
    print """
        # of trials: {}
        # of procs: {}
        Time taken: {}
        Approximated win rate:
            Switch: {}
            Not switch: {}
        """.format(num_trial, num_proc, time_taken, switch_rate, noswitch_rate)


if __name__ == '__main__':
    main(1000000, 5)
