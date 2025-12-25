from event_manager import EventManager

my_event = EventManager()
returned1 = my_event.get_num_registrations()
expected1 = 0
returned2 = my_event.deregister('Mike')
expected2 = False
returned3 = my_event.register('Mike')
expected3 = True
returned4 = my_event.register('Mike')
expected4 = False
returned5 = my_event.register('John')
expected5 = True
returned6 = my_event.deregister('Mike')
expected6 = True
returned7 = my_event.get_num_registrations()
expected7 = 1

if returned1 != expected1:
    print('Test for task 7 failed because returned1 was:')
    print(repr(returned1))
    print('instead of:')
    print(repr(expected1))
elif returned2 != expected2:
    print('Test for task 7 failed because returned2 was:')
    print(repr(returned2))
    print('instead of:')
    print(repr(expected2))
elif returned3 != expected3:
    print('Test for task 7 failed because returned3 was:')
    print(repr(returned3))
    print('instead of:')
    print(repr(expected3))
elif returned4 != expected4:
    print('Test for task 7 failed because returned4 was:')
    print(repr(returned4))
    print('instead of:')
    print(repr(expected4))
elif returned5 != expected5:
    print('Test for task 7 failed because returned5 was:')
    print(repr(returned5))
    print('instead of:')
    print(repr(expected5))
elif returned6 != expected6:
    print('Test for task 7 failed because returned6 was:')
    print(repr(returned6))
    print('instead of:')
    print(repr(expected6))
elif returned7 != expected7:
    print('Test for task 7 failed because returned7 was:')
    print(repr(returned7))
    print('instead of:')
    print(repr(expected7))
else:
    print('Test for task 7 passed')
