#Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def show(self):
        print([self.start, self.end])

class Solution:
    def merge(self, intervals):
        res = []
        intervals.sort(key = lambda x: x.start)
        for interval in intervals:
            if not res or res[-1].end < interval.start:
                res.append(interval)
            else:
                res[-1].end = max(res[-1].end, interval.end)
        return res

            
if __name__ == "__main__":
    solution = Solution()
    inter1 = Interval(1,4)
    inter2 = Interval(2,8)
    res = solution.merge([inter1, inter2])
    for i in res:
        i.show()