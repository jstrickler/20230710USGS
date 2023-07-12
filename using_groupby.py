from itertools import groupby

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

sorted_fruits = sorted(fruits)
print(f"sorted_fruits: {sorted_fruits}\n")

def first_letter(thing):
    return thing[0]

grouped_fruits = groupby(sorted_fruits, key=first_letter)

print(f"grouped_fruits: {grouped_fruits}\n")

d = {}
for letter, fruits in grouped_fruits:
    d[letter] = list(fruits)
#    print(letter, list(fruits))

print(f"d: {d}")
