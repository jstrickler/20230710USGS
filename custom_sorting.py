fruits = ['pomegranate', 'cherry', 'apricot', 'Apple',
'lemon', 'Kiwi', 'ORANGE', 'lime', 'Watermelon', 'guava', 
'Papaya', 'FIG', 'pear', 'banana', 'Tamarind', 'Persimmon', 
'elderberry', 'peach', 'BLUEberry', 'lychee', 'GRAPE', 'date' ]

f0 = sorted(fruits)
print(f"f0: {f0}\n")

# key function: convert element to desired comparison value
#  str.lower(x)   convert string to lower case
f1 = sorted(fruits, key=str.lower)
print(f"f1: {f1}\n")

animal = "wombat"
w = sorted(animal)
print(f"w: {w}\n")

f2 = sorted(fruits, key=len)
print(f"f2: {f2}\n")

def by_len_and_lower(item: str) -> tuple:
    sort_keys = len(item), item.lower()
    # print(f"sorting {item} as {sort_keys}")
    return sort_keys

f3 = sorted(fruits, key=by_len_and_lower)
print(f"f3: {f3}\n")


people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

def by_name(person):
    return person[1], person[0]

for person in sorted(people, key=by_name):
    print(person)
print('-' * 60)

for person in sorted(people, key=lambda p: (p[1], p[0])):
    print(person)


# lambda param-list: return-value
