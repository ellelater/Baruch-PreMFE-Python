import random


class PlayerBase(object):
    def __init__(self, name):
        self.name = name
        self.chosen = None
        self.switched = None
        self.win = None

    def choose(self):
        raise NotImplementedError

    def switch(self, opened):
        raise NotImplementedError


class RandomPlayer(PlayerBase):
    def __int__(self, name):
        super(RandomPlayer, self).__init__(name)

    def choose(self):
        self.chosen = random.randint(1, 3)
        return self.chosen

    def switch(self, opened):
        self.switched = [True, False][random.randint(0, 1)]
        return self.switched


class DumbPlayer(PlayerBase):
    def __int__(self, name):
        super(DumbPlayer, self).__init__(name)

    def choose(self):
        self.chosen = 0
        return self.chosen

    def switch(self, opened):
        self.switched = False
        return self.switched
