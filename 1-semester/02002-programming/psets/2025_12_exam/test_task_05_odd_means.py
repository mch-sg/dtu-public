import numpy as np
from odd_means import odd_means

M = np.array([[5.5, 2.2, 3.3, 2.2, 3.3],
              [5.8, 7, 8, 2.2, 3.3],
              [10, 0.9, 10, 1.1, 1.2]])
returned = odd_means(M)
expected = np.array([7.1, 7.1, 2.6])

if not np.allclose(returned, expected):
    print('Test for task 5 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 5 passed')
