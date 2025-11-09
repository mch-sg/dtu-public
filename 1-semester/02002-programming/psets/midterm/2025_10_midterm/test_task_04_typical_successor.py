from typical_successor import typical_successor

text = 'Hello world. This usual salutation usually starts programming.'
returned = typical_successor(text, 'l')
expected = 'l'

if returned != expected:
    print('Test for task 4 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 4 passed')