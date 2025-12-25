class SimpleTracker:
    def __init__(self, limit):
        self.limit = limit
        self.nums = []
    
    def add(self, number):
        self.number = number

        if self.number > 0 and self.number <= self.limit: 
            self.nums.append(self.number)
            return True
        else:
            return False

    def reset(self):
        self.nums = []
        self.total = 0
        self.span = 0

    def stats(self):
        if len(self.nums) > 1: self.span = max(self.nums) - min(self.nums)
        else: self.span = 0
        return sum(self.nums), self.span

class AdvancedTracker(SimpleTracker):
    def __init__(self, limit, max_delta):
        self.max_delta = max_delta
        self.limit = limit
        self.nums = []

    def add(self, number):
        self.number = number

        if self.number > 0 and self.number <= self.limit: 
            if len(self.nums) > 0 and abs(self.number - self.nums[-1]) < self.max_delta:
                super().add(number)
                return True
            if len(self.nums) == 0: super().add(number); return True
            return False
        else:
            return False