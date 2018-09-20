class Milk:

    _instances = []
    _day = 0

    def __init__(self, produced_day):
        self.produced_day = produced_day

    @classmethod
    def produce(cls, number=1):
        cls._day += 1
        for i in range(number):
            cls._instances.append(Milk(cls._day))

    def __eq__(self, other):
        if self.produced_day == other.produced_day:
            return True

    @classmethod
    def get_lots(cls):
        return cls._instances


Milk.produce(2)
Milk.produce()
Milk.produce(3)

search_set = Milk.get_lots()
for milk in search_set:
    search_set.remove(milk)
    for milk2 in search_set:
        if milk == milk2:
            print("{} and {} are produced in the same day({}).".format(
                milk,
                milk2,
                milk.produced_day
            ))
