#!/usr/bin/env python
# (c)2015 John Strickler

from abc import ABCMeta, abstractmethod

# more or less an interface
class FlyBase(object, metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass

    def dance(self):
        print("cha cha cha")

class FlyWithWings(FlyBase):
    def fly(self):
        print("Soaring on my wings")

    def dance(self):
        print("do the hustle")

class Flightless(FlyBase):
    def fly(self):
        print("Gee, I can't fly")

    def dance(self):
        super().dance()
        print("va va voom")

class FlyWrong(FlyBase):
    pass

if __name__ == '__main__':
    fww = FlyWithWings()
    fww.fly()

    fl = Flightless()
    fl.fly()

    wrong = FlyWrong()