from first_double_peak import first_double_peak

returned = first_double_peak([1.2, 2.4, 3.1, 2.9, 3.6, 2.3, 1.9, 2.4])
expected = 4

if returned != expected:
    print('Test for task 4 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 4 passed')
