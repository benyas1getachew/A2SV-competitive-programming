import random
class RandomizedSet:

    def __init__(self):
        self.dicts={}

    def insert(self, val: int) -> bool:
        if val in self.dicts.keys():
            return False
        else:
            self.dicts[val]=1
            return True

    def remove(self, val: int) -> bool:
        if val in self.dicts.keys():
            self.dicts.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.dicts.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()