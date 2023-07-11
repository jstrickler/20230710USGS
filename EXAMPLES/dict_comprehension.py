from pprint import pprint

animals = ['OWL', 'Badger', 'bushbaby', 'Tiger', 'Wombat', 'GORILLA', 'AARDVARK']

# {KEY: VALUE for VAR ... in ITERABLE if CONDITION}
d = {a.lower(): len(a) for a in animals}  # Create a dictionary with key/value pairs derived from an iterable

print(d, '\n')

words = ['unicorn', 'stigmata', 'barley', 'bookkeeper']

# d = {w:{c:w.count(c) for c in sorted(w)} for w in words} # Use a nested dictionary comprehension to create a dictionary mapping words to dictionaries which map letters to their counts (could be useful for anagrams)

d = {}
for w in words:
    dtemp = {}
    for c in sorted(w):
        dtemp[c] = w.count(c)
    d[w] = dtemp

pprint(d)



# for word, word_signature in d.items():
#     print(word, word_signature)

d3 = {w:sorted(set(w)) for w in words}
pprint(d3)


data = {
    'VA': {
        'capital': 'Richmond',
        'largest_city': 'Norfolk',
    },
    'NC': {
        'capital': 'Raleigh',
        'largest_city': 'Charlotte',
    }
}
print(f"data['NC']['capital']: {data['NC']['capital']}")




