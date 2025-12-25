def nitrate_levels(filename: str) -> tuple:
    with open(filename) as f: data = f.read().strip().splitlines()
    vlow, low, normal, high, vhigh = 0, 0, 0, 0, 0
    for num in data:
        num = float(num)
        if num <= 4.0 : vlow += 1
        if num > 4.0 and num <= 9.0 : low += 1
        if num > 9.0 and num < 40.0 : normal += 1
        if num >= 40.0 and num < 50.0 : high += 1
        if num >= 50.0 : vhigh += 1
    return vlow, low, normal, high, vhigh