import os
from pattern_count import pattern_count

filename = '1-semester/02002-programming/material/2024_12_exam_all_files/2024_12_exam/files/dna_data_1.txt'
file_exists = os.path.isfile(filename)  

if file_exists:
    returned = pattern_count(filename, 'ACCG')
    expected = 2

    if returned == expected:
        print("Test for task 8 passed")
    else:
        print("Test for task 8 failed because it returned:")
        print(repr(returned))
        print("instead of:")
        print(repr(expected))
else:
    print("Test for task 8 failed because the filename is not pointing to a valid file.")
    