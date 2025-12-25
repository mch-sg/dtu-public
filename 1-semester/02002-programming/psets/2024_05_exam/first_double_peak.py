def first_double_peak(sequence: list[float]) -> int:
    sq = sequence
    for i in range(2, len(sq)-2):
        if (sq[i] > sq[i-1] and sq[i] > sq[i-2]) and (sq[i] > sq[i+1] and sq[i] > sq[i+2]):
            return i
    return -1