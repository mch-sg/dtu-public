class BingoCard():
    def __init__(self, numbers):
        self.numbers = numbers
        self.matched = []

    def match(self, number):
        self.number = number

        if self.number in self.numbers:
            self.matched.append(self.number)
            return True
        else:
            return False

    def unmatched(self):
        if len(self.matched) == len(self.numbers):
            return False
        else:
            return True

    def reset(self):
        self.matched = []

#
# Task 10: Informative Bingo Card
#

class InformativeBingoCard(BingoCard):
    def unmatched(self):
        left = abs(len(self.numbers) - len(self.matched))
        return left