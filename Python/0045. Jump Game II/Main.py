class Solution(object):  #不理解
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        curMax = 0
        curRch = 0
        count = 0
        for i in range(n):
            if curRch < i:
                count += 1
                curRch = curMax
            curMax = max(curMax, i + nums[i])
        return count
             