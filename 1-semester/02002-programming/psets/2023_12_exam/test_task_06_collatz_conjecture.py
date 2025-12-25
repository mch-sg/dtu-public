from collatz_conjecture import collatz_conjecture

returned = collatz_conjecture(3)
expected = 7

if returned != expected:
    print('Test for task 6 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 6 passed')
