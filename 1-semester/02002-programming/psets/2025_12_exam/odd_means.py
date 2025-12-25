import numpy as np
def odd_means(M):
    row, col = np.shape(M)
    mean = sum(M[:,::2]) / row
    return mean