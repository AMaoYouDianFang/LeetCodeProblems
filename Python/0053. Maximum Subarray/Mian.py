# 动态规划（只关注：当前值 和 当前值+过去的状态，是变好还是变坏，一定是回看容易理解）
# ms(i) = max(ms[i-1]+ a[i],a[i])
# 到i处的最大值两个可能，一个是加上a[i], 另一个从a[i]起头，重新开始。可以AC
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxSum = [nums[0] for i in range(n)]
        print(maxSum)
        for i in range(1, n):
            maxSum[i] = max(maxSum[i - 1] + nums[i], nums[i])
            #到i处的最大值两个可能，一个是加上a[i], 另一个从a[i]起头，重新开始
        return max(maxSum)

if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-5,-1,-3,-4,-1,-2,-1,-5,-4]))