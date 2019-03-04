import collections
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cache = collections.defaultdict(set) #注意是set
        self.lst = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.lst.append(val)
        self.cache[val].add[len(self.lst)-1]
        return len(self.cache[val]) ==1
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if self.cache[val]:
            idx =self.cache[val].pop()
            self.lst[idx] = self.lst[-1]
            #先加入后删除
        # order of two lines below can not be changed
            # we have to consider there is a condition, self.lst only have one val
            # and val is at the end of our self.lst
            self.cache[self.lst[-1]].add(idx)
            self.cache[self.lst[-1]].discard(len(self.lst) - 1) #删除最后一个index
            self.lst.pop()
            return True
        return False

            
        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.lst)
        