from itertools import chain

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

more_fruits = 'raspberry', 'durian', 'mangosteen'

other_fruits = (f.upper() for f in ['grapefruit', 'mandarin', 'plum'])

for fruit in chain(fruits, more_fruits, other_fruits):
    print(fruit)
print('-' * 60)

stuff = [fruits, more_fruits, other_fruits]

for fruit in chain.from_iterable(stuff):
    print(fruit.title())







