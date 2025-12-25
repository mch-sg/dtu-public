def reservoir_levels(levels: list[int]) -> list[int]:
    arr = []
    for i in range(1,len(levels)):
        if (levels[i-1] - levels[i]) > 150: arr.append(i)
    return arr