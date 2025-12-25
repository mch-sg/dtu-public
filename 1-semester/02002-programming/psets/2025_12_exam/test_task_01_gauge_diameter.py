import math
from gauge_diameter import gauge_diameter

returned = gauge_diameter(12)
expected = 1.8533610896304256

if not math.isclose(returned, expected):
    print('Test for task 1 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 1 passed')
