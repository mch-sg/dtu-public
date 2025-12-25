from navigation_tracking import navigation_tracking

returned = navigation_tracking([2, 5, 1, 3, 4, 2, 1, 1, 6, 2])
expected = [2, 1, 3, 1, 1, 6, 4]

if returned != expected:
    print('Test for task 6 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 6 passed')
