from collections import Counter

state_counter = Counter()
with open('DATA/presidents.txt') as potus_in:
    for raw_line in potus_in:
        fields = raw_line.split(':')
        state_counter[fields[6]] += 1

print(state_counter)
print("*" * 60)

with open('DATA/presidents.txt') as potus_in:
    all_states = [line.split(':')[6] for line in potus_in]
    state_counter = Counter(all_states)
print(state_counter)
