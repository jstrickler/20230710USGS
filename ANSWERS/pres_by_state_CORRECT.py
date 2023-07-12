from pprint import pprint
from itertools import groupby

pres_data = []
with open('../DATA/presidents.txt') as presidents_in:
    for raw_line in presidents_in:
        line = raw_line.rstrip()
        record = line.split(':')
        pres_data.append(record)
    
# pprint(pres_data)

def by_state(p):
    return p[6]

sorted_pres_data = sorted(pres_data, key=by_state)

# pprint(sorted_pres_data)


grouped_pres_data = groupby(sorted_pres_data, key=by_state)

for state, potus_data_iter in grouped_pres_data:
    potus_data = list(potus_data_iter)
    print(f"{state:20s} {len(potus_data):2d}")
