from dice_fairness import dice_fairness

throws = [4, 2, 4, 4, 5, 6, 1, 2, 3, 4, 2, 3, 5, 5, 4, 4, 3, 2, 1, 4, 6]
returned = dice_fairness(throws)
expected = (4, 7, 5)

if returned != expected:
    print('Test for task 5 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 5 passed')