import numpy as np
from robust_values import robust_values

x = np.array([41.42, 44.32, 45.56, 63.01, 12.22, 42.82, 43.73, 40.11])
returned = robust_values(x)
expected = np.array([41.42, 44.32, 45.56, 42.82, 43.73, 40.11])

if not np.allclose(returned, expected):
    print('Test for task 5 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 5 passed')
