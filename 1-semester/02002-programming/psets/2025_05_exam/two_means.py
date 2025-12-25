import numpy as np
def two_means(numbers, threshold: float) -> tuple:
    below = numbers[numbers < threshold]
    above = numbers[numbers > threshold]

    if len(below) == 0: 
        below_mean = threshold
    else: below_mean = np.mean(below)

    if len(above) == 0:
        above_mean = threshold
    else: above_mean = np.mean(above)

    return (below_mean, above_mean)