import math
import numpy as np
from weighted_average import weighted_average

returned = weighted_average(np.array([4.8, 6.6, 12.2, 7.3, 6.5]))
expected = np.float64(6.748513328262833)

if math.isclose(returned, expected):
    print("Test for task 7 passed")
else:
    print("Test for task 7 failed because it returned:")
    print(repr(returned))
    print("instead of:")
    print(repr(expected))
