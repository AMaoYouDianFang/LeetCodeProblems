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

def findRightInterval(self, intervals):
    	sorted_start = [(interval.start, index) for (index, interval) in enumerate(intervals)]
	sorted_start.sort()
	result = []
	
	for interval in intervals:
		end = interval.end
		lo = 0
		hi = len(intervals)
		while lo < hi:
			mid = (lo + hi) // 2
			if sorted_start[mid][0] < end:
				lo = mid+1
			else:
				hi = mid
		if lo == len(intervals):
			result.append(-1)
		else:
			result.append(sorted_start[lo][1])
			
	return result
    

