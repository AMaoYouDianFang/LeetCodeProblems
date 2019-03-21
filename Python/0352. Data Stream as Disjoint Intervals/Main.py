# 题说有个数据流每次提供一个数字，然后让我们组成一系列分离的区间，
# 这道题跟之前那道Insert Interval很像，思路也很像，
# 每进来一个新的数字val，我们都生成一个新的区间[val, val]，
# 然后将其插入到当前的区间里，注意分情况讨论，无重叠，相邻，和有重叠分开讨论处理

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.v = [] 
        

    def addNum(self, val: int) -> None:
        cur = Interval(val, val)
        res = []
        pos = 0
        for i in self.v:
            if cur.end + 1 < i.start: #没有重叠
                res.append(i)
            elif cur.start > i.end +1:
                res.append(i)
                pos +=1
            else:
                cur.start = min(cur.start, i.start)
                cur.end = max(cur.end, i.end)
        res.insert(pos, cur)
        self.v = res
        

    def getIntervals(self):
        for i in self.v:
            print(i.start, i.end, ' ')
        return self.v
        


# Your SummaryRanges object will be instantiated and called as such:
obj = SummaryRanges()
obj.addNum(1)
obj.addNum(2)
param_2 = obj.getIntervals()
