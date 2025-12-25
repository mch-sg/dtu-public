from event_manager import LimitedEventManager

my_event = LimitedEventManager(3)
returned1 = my_event.register('Mike')
expected1 = True
returned2 = my_event.register('Emily')
expected2 = True
returned3 = my_event.register('Sara')
expected3 = True
returned4 = my_event.register('Peter')
expected4 = False
returned5 = my_event.get_num_registrations()
expected5 = 3

if returned1 != expected1:
    print('Test for task 10 failed because returned1 was:')
    print(repr(returned1))
    print('instead of:')
    print(repr(expected1))
elif returned2 != expected2:
    print('Test for task 10 failed because returned2 was:')
    print(repr(returned2))
    print('instead of:')
    print(repr(expected2))
elif returned3 != expected3:
    print('Test for task 10 failed because returned3 was:')
    print(repr(returned3))
    print('instead of:')
    print(repr(expected3))
elif returned4 != expected4:
    print('Test for task 10 failed because returned4 was:')
    print(repr(returned4))
    print('instead of:')
    print(repr(expected4))
elif returned5 != expected5:
    print('Test for task 10 failed because returned5 was:')
    print(repr(returned5))
    print('instead of:')
    print(repr(expected5))
else:
    print('Test for task 10 passed')
