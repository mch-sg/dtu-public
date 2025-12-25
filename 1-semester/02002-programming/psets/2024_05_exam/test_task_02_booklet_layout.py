from booklet_layout import booklet_layout

returned = booklet_layout(17)
expected = (20, 3)

if returned != expected:
    print('Test for task 2 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 2 passed')
