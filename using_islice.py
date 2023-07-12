from itertools import islice

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

fgen = (f.upper() for f in fruits)

print(f"fgen: {fgen}")

fslice = islice(fgen, 2, 4) 
print(f"list(fslice): {list(fslice)}")

for fruit in fgen:
    print(fruit)
