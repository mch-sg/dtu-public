from stock_status import stock_status

returned = stock_status(4, 7)
expected = 'Only 4 left in stock'

if returned != expected:
    print('Test for task 2 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 2 passed')