import os

path = '1-semester/02002-programming/exam/2025_12_exam_all_files/2025_12_exam/files/sentences_1.txt'
if not os.path.isfile(path):
    print('Test for task 7 failed because path could not be found.')
    print('This does not indicate anything about the correctness of your code.')
    print('Please open the correct directory in VSCode (as described under `Solving Exam Tasks` in the pdf), or modify the path above.')
    exit(1)

from sentence_complexities import sentence_complexities

returned = sentence_complexities(path)
expected = [9, 18, 7, 16]

if returned != expected:
    print('Test for task 7 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 7 passed')
