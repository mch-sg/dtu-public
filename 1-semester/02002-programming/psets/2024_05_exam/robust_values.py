import numpy as np
def robust_values(x):
    topdev = np.mean(x) + np.std(x)
    botdev = np.mean(x) - np.std(x)
    arr = np.array([])

    arr = x[botdev <=  x]
    arr = arr[arr <= topdev]

    return arr