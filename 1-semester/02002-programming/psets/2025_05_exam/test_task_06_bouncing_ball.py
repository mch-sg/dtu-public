from bouncing_ball import bouncing_ball

returned = bouncing_ball(2.5)
expected = 3

if returned != expected:
    print('Test for task 6 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 6 passed')
