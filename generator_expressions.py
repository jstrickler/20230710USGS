fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

fgen1 = (f.upper() for f in fruits)
print(f"fgen1: {fgen1}")

fgen2 = (f[:3] for f in fgen1)
print(f"fgen2: {fgen2}")

for fruit in fgen2:
    print(fruit)



