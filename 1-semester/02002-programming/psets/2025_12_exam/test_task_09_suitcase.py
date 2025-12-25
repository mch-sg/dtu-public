from suitcase import Suitcase

carry_on = Suitcase(7.0)
check_in = Suitcase(23.0)
returned1 = carry_on.pack_item('Laptop', 1.5)
expected1 = True
returned2 = check_in.pack_item('Clothes', 5.0)
expected2 = True
returned3 = check_in.pack_item('E-Bike', 20.0)
expected3 = False
all_luggage = carry_on + check_in
returned4 = all_luggage.currently_packed()
expected4 = ['Laptop', 'Clothes']

if returned1 != expected1:
    print('Test for task 9 failed because returned1 was:')
    print(repr(returned1))
    print('instead of:')
    print(repr(expected1))
elif returned2 != expected2:
    print('Test for task 9 failed because returned2 was:')
    print(repr(returned2))
    print('instead of:')
    print(repr(expected2))
elif returned3 != expected3:
    print('Test for task 9 failed because returned3 was:')
    print(repr(returned3))
    print('instead of:')
    print(repr(expected3))
elif returned4 != expected4:
    print('Test for task 9 failed because returned4 was:')
    print(repr(returned4))
    print('instead of:')
    print(repr(expected4))
else:
    print('Test for task 9 passed')
