import math
from parallel_resistors import parallel_resistors

returned = parallel_resistors([10.5, 12.5, 50.0])
expected = 5.121951219512195

if not math.isclose(returned, expected):
    print('Test for task 3 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 3 passed')
