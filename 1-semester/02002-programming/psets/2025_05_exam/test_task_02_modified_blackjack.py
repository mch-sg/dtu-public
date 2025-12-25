from modified_blackjack import modified_blackjack

returned = modified_blackjack([5, 2, 3, 9, 7, 6, 2, 4])
expected = (1, 4)

if returned != expected:
    print('Test for task 2 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 2 passed')
