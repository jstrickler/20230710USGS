
x = "foo:bar:blah"

fields = x.split(':')

print(f"fields: {fields}")
print()



with open('DATA/knights.txt') as knights_in:
    my_data = []
    for raw_line in knights_in:
        line = raw_line.rstrip()   # remove newline
        # print(line)
        my_data.append(tuple(line.split(':')))

print(my_data)
print('-' * 60)

with open('DATA/knights.txt') as knights_in:
    more_data = [tuple(line.rstrip().split(':')) for line in knights_in]
    
print(more_data)


