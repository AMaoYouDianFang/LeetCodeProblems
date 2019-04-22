#2-13
# Definition for an interval.
from typing import List

class Solution:
    ##第一个方法超时了
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        res = []
        v = [] #用于存放start元素
        l = len(intervals)
        dic = {}
        for i in range(l):
            dic[intervals[i][0]] = i
            v.append(intervals[i][0])
        v.sort(reverse = True)
        for i in range(l):
            for j in range(l):
                if v[j] < intervals[i][1]:
                    break
            if j == 0:
                res.append(-1)
            else:
                res.append(dic[v[j-1]]) #一开始这里写错
        return res

        
    #下面的代没有超时，二分法见总结
    def findRightInterval(self, intervals):
        sorted_start = [(interval[0], index) for index, interval in enumerate(intervals)]
        sorted_start.sort()
        res = []
        for interval in intervals:
            target = interval[1]
            l = 0
            r = len(intervals) 
            while l <= r:
                mid = (l + r) //2
                if sorted_start[mid][0] < target:
                    l = mid + 1
                else:
                    r = mid
            if l == len(intervals):
                res.append(-1)
            else:
                res.append(sorted_start[l][0])
        return res
           
    

