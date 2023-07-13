
def  simple():
    yield "generators"
    yield "are"
    yield "fun"

s = simple()
print(f"s: {s}")
print(f"type(s): {type(s)}")

for word in s:
    print(word)

