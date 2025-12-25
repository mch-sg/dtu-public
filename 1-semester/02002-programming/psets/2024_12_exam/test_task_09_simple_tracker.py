from simple_tracker import SimpleTracker

tracker = SimpleTracker(500)
returned1 = tracker.add(510)
returned2 = tracker.add(200)
returned3 = tracker.add(352)
returned4 = tracker.stats()
tracker.reset()
returned5 = tracker.stats()

expected1 = False
expected2 = True
expected3 = True
expected4 = 552, 152
expected5 = 0, 0

if ((returned1 == expected1) and (returned2 == expected2) and 
    (returned3 == expected3) and (returned4 == expected4) and 
    (returned5 == expected5)):
    print("Test for task 9 passed")
else:
    print("Test for task 9 failed because it returned:")
    print(repr(returned1), repr(returned2), repr(returned3), repr(returned4), repr(returned5))
    print("instead of:")
    print(repr(expected1), repr(expected2), repr(expected3), repr(expected4), repr(expected5))
