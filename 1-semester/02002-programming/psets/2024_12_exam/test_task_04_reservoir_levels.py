from reservoir_levels import reservoir_levels

returned = reservoir_levels([1320, 1307, 1295, 1102, 1360, 1395, 1101, 1208])
expected = [3, 6]

if returned == expected:
    print("Test for task 4 passed")
else:
    print("Test for task 4 failed because it returned:")
    print(repr(returned))
    print("instead of:")
    print(repr(expected))
