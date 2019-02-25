# 题说有个数据流每次提供一个数字，然后让我们组成一系列分离的区间，
# 这道题跟之前那道Insert Interval很像，思路也很像，
# 每进来一个新的数字val，我们都生成一个新的区间[val, val]，
# 然后将其插入到当前的区间里，注意分情况讨论，无重叠，相邻，和有重叠分开讨论处理

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def addNum(self, val):
        

    def getIntervals(self):
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()