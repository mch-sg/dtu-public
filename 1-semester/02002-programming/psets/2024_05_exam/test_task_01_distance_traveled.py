import math
from distance_traveled import distance_traveled

returned = distance_traveled(5.5)
expected = 148.37625

if not math.isclose(returned, expected):
    print('Test for task 1 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 1 passed')
