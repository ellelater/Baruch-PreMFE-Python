from player import RandomPlayer, DumbPlayer
from game import MontyHallGame
import logging


def main():
    logging.basicConfig(level=logging.DEBUG)
    g = MontyHallGame()
    p = RandomPlayer('Elle')
    print g.play(p)


if __name__ == '__main__':
    main()
