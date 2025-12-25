def event_probability(T: int, n: int) -> float:
    P = 1 - (1- (1/T))**(n)
    return P