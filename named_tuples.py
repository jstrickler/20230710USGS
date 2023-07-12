from collections import namedtuple
from dataclasses import dataclass

# gage_id  flow  date 

x = 123, '2023-07-04'

print(f"x: {x}")

print(f"x[0]: {x[0]}")
print(f"x[1]: {x[1]}")

Gage = namedtuple('Gage', "flow date")

x = Gage(456, '2023-07-12')
print(f"x.flow: {x.flow}")
print(f"x.date: {x.date}")

@dataclass
class GageInfo:
    flow: float
    date: str

    def can_paddle(self):
        return True

g = GageInfo(329, '2023-07-06')
print(g.date, g.flow)
print(g.can_paddle())



