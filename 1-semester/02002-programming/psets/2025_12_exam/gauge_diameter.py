import math
def gauge_diameter(n: int) -> float:
    V = 40
    d3 = (6 * V) / (n * math.pi)
    d = d3 ** (1/3)
    return d