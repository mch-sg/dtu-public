import math
from compound_interest import compound_interest

returned = compound_interest(1500, 0.04, 8)
expected = 61.06056588815591

if not math.isclose(returned, expected):
    print('Test for task 1 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 1 passed')