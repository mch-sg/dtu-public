import math
from punctuation_ratio import punctuation_ratio

text = ("Sara and Emma like to travel, bike, and hike, and when they are " +
    "traveling they always take their bikes, hiking shoes, and sleeping bags. " +
    "Last year, Sarah and Emma traveled to Italy, France, and Spain. And that " +
    "was fun, and, according to Sara and Emma, very expensive!")
returned = punctuation_ratio(text)
expected = 1.3333333333333333

if not math.isclose(returned, expected):
    print('Test for task 4 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 4 passed')
