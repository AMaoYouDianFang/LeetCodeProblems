#Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def show(self):
        print([self.start, self.end])

class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort( key = lambda x : x.start )
        for i in range (1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    inter1 = [Interval(1,30), Interval(5,10), Interval(15,20)]
    inter2 = [Interval(7,10), Interval(2,4)]
    res = solution.canAttendMeetings(inter1)
    print(res)

