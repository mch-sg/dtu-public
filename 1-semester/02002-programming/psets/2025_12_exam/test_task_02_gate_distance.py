from gate_distance import gate_distance

returned = gate_distance('A8', 'B5')
expected = 'Walking time 15 min'

if returned != expected:
    print('Test for task 2 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 2 passed')
