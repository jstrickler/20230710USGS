
#  struct person {
#     char *firstname;
#     char *lastname;
#  }

x = 5, 8
y = 5,
z = ()
t = (9, 22, 44)

print(type(x), type(y), type(z))

person = "Bill", "Gates", "Microsoft", "1955-10-28"
print(f"len(person): {len(person)}")
print(f"person[0]: {person[0]}")

# print(f"x: {x}")
print(person[0], person[1])

#  "iterable"

first_name, last_name, product, dob = person    # iterable unpacking


people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
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
    ('Linus', 'Torvalds', 'Linux', "git", '1969-12-28'),
    ('John', 'Strickler', '19xx-xx-xx'),
]
print(f"people[0]: {people[0]}")
print(f"type(people[0]): {type(people[0])}")
print(f"people[0][0]: {people[0][0]}")
print(f"people[0][0][0]: {people[0][0][0]}")

for first_name, last_name, *product, dob in people:
    # first_name, last_name, product, dob = people[0]  first loop
    # first_name, last_name, product, dob = people[1]  second loop
    # etc

    print(first_name, last_name, dob, product)
print()

# for person in people:
#     print(person[0], person[1], person[3])
# print()

values = 'a', 'b', 'c', 'd', 'e', 'f'

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)







