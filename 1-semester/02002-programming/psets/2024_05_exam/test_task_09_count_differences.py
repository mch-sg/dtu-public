import os

filename1 = '1-semester/02002-programming/material/2024_05_exam_all_files/2024_05_exam/files/results_A1.txt'
if not os.path.isfile(filename1):
    print('Test for task 9 failed because filename1 could not be found.')
    print('This does not indicate anything about the correctness of your code.')
    print('Please open the correct directory in VSCode (as described under `Solving Exam Tasks` in the pdf), or modify the path above.')
    exit(1)

from count_differences import count_differences

filename2 = '1-semester/02002-programming/material/2024_05_exam_all_files/2024_05_exam/files/results_A2.txt'
returned = count_differences(filename1, filename2)
expected = 3

if returned != expected:
    print('Test for task 9 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 9 passed')
