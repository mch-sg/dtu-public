from phonebook_merge import phonebook_merge

phonebook = {'Liv': ['55511112', '18777890'] ,
             'Mads': ['27274445', '48533336'],
             'Steve': ['45455555', '25455525']}
second_phonebook = {'Anna': ['89577772'] ,
                    'Steve': ['25257755', '25455525'],
                    'Mads': ['48533336', '27274445']}
phonebook_merge(phonebook, second_phonebook)
returned = phonebook
expected = {'Liv': ['55511112', '18777890'],
            'Mads': ['27274445', '48533336'],
            'Steve': ['45455555', '25455525', '25257755'],
            'Anna': ['89577772']}

if returned != expected:
    print('Test for task 8 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 8 passed')
