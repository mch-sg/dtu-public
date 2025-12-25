import math
def polygon_area(n: int, s: float) -> float:
    A = (n*s**2) / (4 * math.tan(math.pi/n))
    return A