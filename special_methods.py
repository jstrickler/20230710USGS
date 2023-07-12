

class Thing: # inherits from object
    def __str__(self):
        return "a thing"

    def __len__(self):
        return 100
    
    def __add__(self, other):
        return "wombat"


t = Thing()
print(f"t: {t}")

x = str(t)

print(f"len(t): {len(t)}")

t2 = Thing()

print(f"t + t2: {t + t2}")
