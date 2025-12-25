from graph_transpose import graph_transpose

graph = {
    2: [1],
    1: [2, 4],
    3: [1, 2],
}
returned = graph_transpose(graph)
expected = {1: [2, 3], 2: [1, 3], 4: [1]}

if returned != expected:
    print('Test for task 4 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 4 passed')
