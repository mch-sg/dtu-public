from photo_details import photo_details

returned = photo_details('20250305_110031.jpg')
expected = {'year': '2025', 'month': '03', 'day': '05', 'number': '110031', 'ext': 'jpg'}

if returned != expected:
    print('Test for task 4 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 4 passed')
