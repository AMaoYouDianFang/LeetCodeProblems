class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res = [0] * (length+1)
        
        for start, end, inc in updates:
            res[start] += inc
            res[end+1] -= inc
        
        for i in range(1, length):
            res[i] += res[i-1]
        return res[:-1]