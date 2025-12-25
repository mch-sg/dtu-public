import math
import numpy as np
from two_means import two_means

returned = two_means(np.array([1.5, 8.5, 3.5, 4.5, 5.0, 6.5, 7.5, 2.5, 1.0]), 5.5)
expected = (3.0, 7.5)

if len(returned) != len(expected) or not math.isclose(returned[0], expected[0]) or not math.isclose(returned[1], expected[1]):
    print('Test for task 8 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 8 passed')
