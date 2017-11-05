class Asset(object):
    def __init__(self, val):
        self.val = val

    def year_dep_rate(self):
        return 0.1

    def mon_dep_rate(self):
        return self.year_dep_rate() / 12

    def current_val(self, period):
        total_dep = (1 - self.mon_dep_rate()) ** period
        return self.val * total_dep

    def annualDepRate(self):
        raise NotImplementedError()


class Car(Asset):
    def __init__(self, val):
        super(Car, self).__init__(val)
        self._dep_rate = 0.2


class Civic(Car):
    def __init__(self, val):
        super(Civic, self).__init__(val)
        self._dep_rate = 0.01


class Z4(Car):
    def __init__(self, val):
        super(Z4, self).__init__(val)
        self._dep_rate = 0.3


class HouseBase(Asset):
    def __init__(self, val):
        super(HouseBase, self).__init__(val)
        self._dep_rate = 0.1


class PrimaryHome(HouseBase):
    def __init__(self, val):
        super(PrimaryHome, self).__init__(val)
        self._dep_rate = 0.4


class VacationHome(HouseBase):
    def __init__(self, val):
        super(VacationHome, self).__init__(val)
        self._dep_rate = 0.05
