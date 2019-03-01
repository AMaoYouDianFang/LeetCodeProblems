import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cache = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.cache:
            self.lst.append(val)
            self.cache[val] = len(self.lst) -1
            return True
        return False
        

    def remove(self, val: int) -> bool: #删除元素时间是常数的O（1）
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.lst:
            idx = self.cache[val]
            self.lst[idx] = self.lst[-1]
            self.cache[self.lst[idx]] = idx
            self.lst.pop()
            del self.cache[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.lst)

