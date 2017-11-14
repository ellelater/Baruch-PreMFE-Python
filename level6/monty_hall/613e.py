from player import RandomPlayer, DumbPlayer
from game import MontyHallGame
import logging


def main():
    logging.basicConfig(level=logging.ERROR)
    g = MontyHallGame()
    p = RandomPlayer('Elle')

    switch_result = [0., 0]
    noswitch_result = [0., 0]
    for trial in xrange(1000):
        result = g.play(p)
        if p.switched:
            switch_result[1] += 1
            switch_result[0] += result
        else:
            noswitch_result[1] += 1
            noswitch_result[0] += result
    print """
    Approximation results:
        Switch: {}
        Not switch: {}
    """.format(switch_result[0]/switch_result[1], noswitch_result[0] / noswitch_result[1])


if __name__ == '__main__':
    main()
