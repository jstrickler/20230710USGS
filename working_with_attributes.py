from president import President

p = President(1)

print(p)
print(p.first_name, p.last_name, p.birth_state)

field_name = "party"

print(f"getattr(p, field_name): {getattr(p, field_name)}")

# getattr(obj, name) 
# hasattr(obj, name)
# setattr(obj, name, value)
# delattr(obj, name)

def get_full_name(self):
    return f"{self.first_name} {self.last_name}"

setattr(President, "get_full_name", get_full_name)

print(f"p.get_full_name(): {p.get_full_name()}")

print(dir(p), '\n')

# delattr(p, "party")

print(p.party)

delattr(President, "party")


def convert_to_json(obj):
    if hasattr(obj, 'to_json'):
        json_data = obj.to_json()
    else:
        # convert manually
        json_data = None
        
