import math
from event_probability import event_probability

returned = event_probability(100, 25)
expected = 0.22217864060085335

if not math.isclose(returned, expected):
    print('Test for task 1 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 1 passed')
