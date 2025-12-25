from bank_account import BankAccount

my_account = BankAccount(1000)
returned1 = my_account.get_balance()
expected1 = 1000
my_account.deposit(500)
returned2 = my_account.get_balance()
expected2 = 1500
returned3 = my_account.withdraw(200)
expected3 = 200
returned4 = my_account.get_balance()
expected4 = 1300
returned5 = my_account.withdraw(2000)
expected5 = 0
returned6 = my_account.get_balance()
expected6 = 1300

if returned1 != expected1:
    print('Test for task 7 failed because returned1 was:')
    print(repr(returned1))
    print('instead of:')
    print(repr(expected1))
elif returned2 != expected2:
    print('Test for task 7 failed because returned2 was:')
    print(repr(returned2))
    print('instead of:')
    print(repr(expected2))
elif returned3 != expected3:
    print('Test for task 7 failed because returned3 was:')
    print(repr(returned3))
    print('instead of:')
    print(repr(expected3))
elif returned4 != expected4:
    print('Test for task 7 failed because returned4 was:')
    print(repr(returned4))
    print('instead of:')
    print(repr(expected4))
elif returned5 != expected5:
    print('Test for task 7 failed because returned5 was:')
    print(repr(returned5))
    print('instead of:')
    print(repr(expected5))
elif returned6 != expected6:
    print('Test for task 7 failed because returned6 was:')
    print(repr(returned6))
    print('instead of:')
    print(repr(expected6))
else:
    print('Test for task 7 passed')
