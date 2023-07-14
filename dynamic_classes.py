
class Animal:
    def run(self):
        print("running running ...")

Dog = type('Dog', (Animal,), {'speak': lambda self: print("woof")})
Cat = type('Cat', (Animal,), {'speak': lambda self: print("meow")})

d = Dog()
d.speak()

c = Cat()
c.speak()