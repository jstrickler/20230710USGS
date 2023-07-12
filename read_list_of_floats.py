
from functools import reduce
from operator import add

with open('DATA/float_values.txt') as floats_in:
    raw_values = floats_in.read().splitlines()

total = reduce(add, map(float, raw_values))
print(f"total: {total}")
