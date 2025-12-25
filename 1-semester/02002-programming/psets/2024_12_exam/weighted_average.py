import numpy as np
def weighted_average(x) -> float:
    mean = np.mean(x)
    std = np.std(x)
    if np.std(x) == 0: std = np.mean(x)
    weight = np.exp((-(x-mean)**2)/(2*std**2))
    return sum(weight*x) / sum(weight)
