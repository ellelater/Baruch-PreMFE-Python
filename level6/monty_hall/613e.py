from player import RandomPlayer, DumbPlayer
from game import MontyHallGame
import logging
import time


def main(num_trial):
    logging.basicConfig(level=logging.ERROR)
    g = MontyHallGame()
    p = RandomPlayer('Elle')

    switch_result = [0., 0]
    noswitch_result = [0., 0]
    start = time.time()
    for trial in xrange(num_trial):
        result = g.play(p)
        if p.switched:
            switch_result[1] += 1
            switch_result[0] += result
        else:
            noswitch_result[1] += 1
            noswitch_result[0] += result
    time_taken = time.time() - start
    print """
    # of trials: {}
    Time taken: {}
    Approximated win rate:
        Switch: {}
        Not switch: {}
    """.format(num_trial,
               time_taken,
               switch_result[0]/switch_result[1],
               noswitch_result[0] / noswitch_result[1])


if __name__ == '__main__':
    main(1000000)
