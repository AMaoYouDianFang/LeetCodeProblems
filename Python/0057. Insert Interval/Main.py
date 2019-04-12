#Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def show(self):
        print([self.start, self.end])

class Solution:
    def insert(self, intervals, newInterval):
        l, r = 0,0 #表示有重复元素的区间
        s = newInterval.start
        e = newInterval.end

        for i in intervals:
            if e < i.start:  # e 小于起点
                break
            elif s > i.end:  #s大于终点
                l += 1
                r += 1
            else:        #有交叉
                s = min(i.start, s)
                e = max(e,i.end)
                r +=1
        return intervals[:l] + [Interval(s, e)] + intervals[r:]

if __name__ == "__main__":
    solution = Solution()
    inter1 = Interval(1,3)
    inter2 = Interval(6,9)
    res = solution.insert([inter1, inter2], Interval(2,5))
    for i in res:
        i.show()