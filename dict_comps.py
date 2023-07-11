"""
dictionary comprehension examples
"""
# { key:value for var in iterable}

fruits = ['pomegranate', 'cherry', 'apricot', 'Apple',
'lemon', 'Kiwi', 'ORANGE', 'lime', 'Watermelon', 'guava',
'Papaya', 'FIG', 'pear', 'banana', 'Tamarind', 'Persimmon',
'elderberry', 'peach', 'BLUEberry', 'lychee', 'GRAPE', 'date' ]

d = {f.lower(): len(f) for f in fruits}
print(f"d: {d}\n")

values = {'a': 10, 'b': 36, 'c': 42}
flipped = {y:x for x, y in values.items()}
print(f"flipped: {flipped}\n")
