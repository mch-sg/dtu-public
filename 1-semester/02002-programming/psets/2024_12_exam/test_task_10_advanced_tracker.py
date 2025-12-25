from simple_tracker import AdvancedTracker

tracker = AdvancedTracker(500, 100)
returned1 = tracker.add(200)
returned2 = tracker.add(352)
returned3 = tracker.add(252)
returned4 = tracker.stats()
returned5 = tracker.add(510)

expected1 = True
expected2 = False
expected3 = True
expected4 = 452, 52
expected5 = False

if ((returned1 == expected1) and (returned2 == expected2) and 
    (returned3 == expected3) and (returned4 == expected4) and 
    (returned5 == expected5)):
    print("Test for task 10 passed")
else:
    print("Test for task 10 failed because it returned:")
    print(repr(returned1), repr(returned2), repr(returned3), repr(returned4), repr(returned5))
    print("instead of:")
    print(repr(expected1), repr(expected2), repr(expected3), repr(expected4), repr(expected5))
