import numpy as np
def checkerboard_sum(A) -> float:
    res = 0
    if A[::2][:,::2].size > 0: res += sum(A[::2][:,::2])
    if A[1::2][:,1::2].size > 0: res += sum(A[1::2][:,1::2])
    return sum(res)
