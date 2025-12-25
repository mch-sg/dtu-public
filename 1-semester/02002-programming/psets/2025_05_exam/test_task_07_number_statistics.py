import os

filename = '1-semester/02002-programming/material/2025_05_exam_all_files/2025_05_exam/files/numbers_1.txt'
if not os.path.isfile(filename):
    print('Test for task 7 failed because filename could not be found.')
    print('This does not indicate anything about the correctness of your code.')
    print('Please open the correct directory in VSCode (as described under `Solving Exam Tasks` in the pdf), or modify the path above.')
    exit(1)

from number_statistics import number_statistics

returned = number_statistics(filename, 8)
expected = [1, 0, 2]

if returned != expected:
    print('Test for task 7 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 7 passed')
