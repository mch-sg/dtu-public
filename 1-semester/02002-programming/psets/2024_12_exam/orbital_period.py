import math
def orbital_period(a: float, M: float) -> float:
    G = 6.6743*10**(-11)
    Tsqr = (4*(math.pi)**2)/(G*M)*a**3
    return math.sqrt(Tsqr)