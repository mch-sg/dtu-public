def parallel_resistors(resistances: list[float]) -> float:
    ressum = 0
    for num in resistances:
        ressum += 1 / num
    
    return 1 / ressum