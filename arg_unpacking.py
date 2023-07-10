

def doit(x, y):
    print(f"x: {x}")
    print(f"y: {y}")
    
doit(5, 10)
doit('red', 'blue')
# doit(1, 2, 3)

values = [19, 37]
doit(*values)  # argument unpacking

name = "Bob"
print(f"name: {name}")

city = "Bedrock"

print("Fred Flintstone,", city)
print("Fred Flintstone,{}".format(city))
m = "Fred Flintstone,{}".format(city)
print("Fred Flintstone,%s" % (city))

print(f"Fred Flintstone,{city}")
value = 39.3745983
print(f"value is {value:.2f}")
big_number = 32039523098923
print(f"big number: {big_number:,d}")

print(f"2 + 2 is {2 + 2}")







