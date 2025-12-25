class Suitcase():
    def __init__(self, weight_limit):
        self.weight_limit = weight_limit
        self.packed = []
        self.allweights = []

    def pack_item(self, item: str, weight: float) -> bool:
        self.item = item
        self.weight = weight

        if sum(self.allweights) + self.weight > self.weight_limit:
            return False
        
        self.allweights.append(self.weight)
        self.packed.append(self.item)
        return True

    def __add__(self, other):
        self.newsuit = Suitcase(self.weight_limit + other.weight_limit)

        self.newsuit.packed.extend(self.packed)
        self.newsuit.packed.extend(other.packed)
        return self.newsuit

    def currently_packed(self) -> list:
        return self.packed