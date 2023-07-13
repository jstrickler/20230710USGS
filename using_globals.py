from pprint import pprint

hero = "Spiderman"
villain = "Thanos"

not_sure = "Deadpool"

class Ham:
    pass

def spam():
    print("SPAM SPAM SPAM")

g = globals()
pprint(g)

print(f"g['spam']: {g['spam']}")

g['spam']()

h = g['Ham']()
print(f"h: {h}")

g['color'] = 'mauve'
print(f"color: {color}")

g['bark'] = lambda : print("woof woof")

bark()

def toast():
    x = 5
    name = "Bob"
    print(f"locals(): {locals()}")

toast()