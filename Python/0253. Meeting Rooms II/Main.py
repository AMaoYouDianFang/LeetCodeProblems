#Definition for an interval.
from heapq import heappop, heappush
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def show(self):
        print([self.start, self.end])

class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        res = []  
        intervals.sort(key = lambda x:x.start)
        for i in intervals:
            if res and res[0] < i.start:
                heappop(res)  #如果结束的早于将要开始的，弹出再加入，不早的话直接加入
            heappush(res,i.end) 
        return len(res)
         

if __name__ == "__main__":
    solution = Solution()
    inter1 = [Interval(0,30), Interval(5,10), Interval(15,20)]
    inter2 = [Interval(7,10), Interval(2,4)]
    res = solution.minMeetingRooms(inter1)
    print(res)