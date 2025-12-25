import math
from polygon_area import polygon_area

returned = polygon_area(5, 4.31)
expected = 31.9597602410807

if not math.isclose(returned, expected):
    print('Test for task 1 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 1 passed')
