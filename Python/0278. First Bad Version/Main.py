#2-15 寻找序列的第一个true
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 1
        e = n
        while s < e:
            mid = ( s + e) //2
            if  isBadVersion(mid) == False:
                s = mid + 1
            else: 
                e = mid
        return s 