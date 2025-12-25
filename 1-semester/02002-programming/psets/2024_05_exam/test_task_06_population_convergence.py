from population_convergence import population_convergence

returned = population_convergence(4.8, 0.65)
expected = 6

if returned != expected:
    print('Test for task 6 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 6 passed')
