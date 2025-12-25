from experiment_numbers import experiment_numbers

returned = experiment_numbers(['A-1', 'A-3', 'B-2', 'A-4', 'B-1', 'B-3', 'N-4'])
expected = {'A': 4, 'B': 3, 'N': 4}

if returned != expected:
    print('Test for task 5 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 5 passed')
