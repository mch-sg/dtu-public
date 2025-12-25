import math
from running_speed import running_speed

returned = running_speed(5.5)
expected = (10.90909090909091, 3.0303030303030307)

if len(returned) != len(expected) or not math.isclose(returned[0], expected[0]) or not math.isclose(returned[1], expected[1]):
    print('Test for task 3 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 3 passed')
