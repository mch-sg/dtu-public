def chamber_pressure(P0: float, Pmax: float, Pcrit: float, k: float) -> int:
    res, indx = 0, 0
    while P0 < Pcrit:
        res = k*(Pmax - P0)
        P0 += res
        indx += 1
    return indx