import random
import logging


class MontyHallGame(object):
    def __init__(self):
        self.prize = random.randint(1, 3)
        logging.debug("Prize is in door {}".format(self.prize))

    def open_door(self, first_choice):
        to_open = {1, 2, 3}
        to_open.discard(self.prize)
        to_open.discard(first_choice)
        opened = random.choice(list(to_open))
        return opened

    def final_choice(self, first_choice, opened, switch):
        if not switch:
            return first_choice
        else:
            remain = {1, 2, 3}
            remain.discard(opened)
            remain.discard(first_choice)
            return remain.pop()

    def play(self, player):
        first_choice = player.choose()
        logging.debug("Player chose door {}".format(first_choice))
        opened = self.open_door(first_choice)
        logging.debug("Door {} is opened.".format(opened))
        switch = player.switch(opened)
        logging.debug("Player chose {}to switch.".format(['not ', ''][switch]))
        final_choice = self.final_choice(first_choice, opened, switch)
        result = (final_choice == self.prize)
        logging.debug("Player {}".format(["didn't win.", "won!"][result]))
        player.win = result
        return result
