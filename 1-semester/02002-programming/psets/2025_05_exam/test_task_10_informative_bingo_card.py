from bingo_card import InformativeBingoCard

card = InformativeBingoCard([15, 27, 73])
returned1 = card.match(27)
expected1 = True
returned2 = card.match(53)
expected2 = False
returned3 = card.match(73)
expected3 = True
returned4 = card.unmatched()
expected4 = 1
returned5 = card.match(15)
expected5 = True
returned6 = card.unmatched()
expected6 = 0
card.reset()
returned7 = card.unmatched()
expected7 = 3

if returned1 != expected1:
    print('Test for task 10 failed because returned1 was:')
    print(repr(returned1))
    print('instead of:')
    print(repr(expected1))
elif returned2 != expected2:
    print('Test for task 10 failed because returned2 was:')
    print(repr(returned2))
    print('instead of:')
    print(repr(expected2))
elif returned3 != expected3:
    print('Test for task 10 failed because returned3 was:')
    print(repr(returned3))
    print('instead of:')
    print(repr(expected3))
elif returned4 != expected4:
    print('Test for task 10 failed because returned4 was:')
    print(repr(returned4))
    print('instead of:')
    print(repr(expected4))
elif returned5 != expected5:
    print('Test for task 10 failed because returned5 was:')
    print(repr(returned5))
    print('instead of:')
    print(repr(expected5))
elif returned6 != expected6:
    print('Test for task 10 failed because returned6 was:')
    print(repr(returned6))
    print('instead of:')
    print(repr(expected6))
elif returned7 != expected7:
    print('Test for task 10 failed because returned7 was:')
    print(repr(returned7))
    print('instead of:')
    print(repr(expected7))
else:
    print('Test for task 10 passed')
