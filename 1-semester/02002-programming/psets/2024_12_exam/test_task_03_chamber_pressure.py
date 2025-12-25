from chamber_pressure import chamber_pressure

returned = chamber_pressure(20, 120, 105, 0.1)
expected = 19

if returned == expected:
    print("Test for task 3 passed")
else:
    print("Test for task 3 failed because it returned:")
    print(repr(returned))
    print("instead of:")
    print(repr(expected))
