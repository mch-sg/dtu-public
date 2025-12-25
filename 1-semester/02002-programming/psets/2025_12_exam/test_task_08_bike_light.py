from bike_light import BikeLight

light = BikeLight()
returned1 = light.long_press()
expected1 = 'weak'
returned2 = light.short_press()
expected2 = 'strong'
returned3 = light.short_press()
expected3 = 'flash'
returned4 = light.long_press()
expected4 = 'off'
returned5 = light.long_press()
expected5 = 'weak'

if returned1 != expected1:
    print('Test for task 8 failed because returned1 was:')
    print(repr(returned1))
    print('instead of:')
    print(repr(expected1))
elif returned2 != expected2:
    print('Test for task 8 failed because returned2 was:')
    print(repr(returned2))
    print('instead of:')
    print(repr(expected2))
elif returned3 != expected3:
    print('Test for task 8 failed because returned3 was:')
    print(repr(returned3))
    print('instead of:')
    print(repr(expected3))
elif returned4 != expected4:
    print('Test for task 8 failed because returned4 was:')
    print(repr(returned4))
    print('instead of:')
    print(repr(expected4))
elif returned5 != expected5:
    print('Test for task 8 failed because returned5 was:')
    print(repr(returned5))
    print('instead of:')
    print(repr(expected5))
else:
    print('Test for task 8 passed')
