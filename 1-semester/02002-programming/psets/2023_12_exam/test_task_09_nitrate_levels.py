import os

path = '1-semester/02002-programming/material/2023_12_exam_all_files/2023_12_exam/files/nitrate_data_A.txt'
if not os.path.isfile(path):
    print('Test for task 9 failed because path could not be found.')
    print('This does not indicate anything about the correctness of your code.')
    print('Please open the correct directory in VSCode (as described under `Solving Exam Tasks` in the pdf), or modify the path above.')
    exit(1)

from nitrate_levels import nitrate_levels

returned = nitrate_levels(path)
expected = (0, 0, 8, 2, 0)

if returned != expected:
    print('Test for task 9 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 9 passed')
