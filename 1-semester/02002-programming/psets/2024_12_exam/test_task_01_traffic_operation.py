from traffic_operation import traffic_operation

returned = traffic_operation(8)
expected = 'rush hour'

if returned == expected:
    print("Test for task 1 passed")
else:
    print("Test for task 1 failed because it returned:")
    print(repr(returned))
    print("instead of:")
    print(repr(expected))
