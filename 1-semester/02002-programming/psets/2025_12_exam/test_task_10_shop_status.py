from shop_status import shop_status

returned = shop_status('Monday', 9)
expected = (True, 'Monday', 17)

if returned != expected:
    print('Test for task 10 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 10 passed')
