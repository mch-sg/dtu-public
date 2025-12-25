def population_convergence(N: float, r: float) -> int:
    K = 10
    years = 0

    while N >= 10.1 or N <= 9.9:
        N = N + r * (1 - (N/K)) * N
        years += 1
    
    return years