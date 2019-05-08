class Solution:
    def rob(self, nums) -> int:
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:  #miss
            return nums[0] 
        d = [None] * len(nums)
        d[0] = nums[0]
        d[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            d[i] = max(d[i-1], d[i-2]+ nums[i])
        return d[len(nums)-1]
     #降低空间复杂度
    def rob1(self, nums) -> int:
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0] 
        pre2 = nums[0]
        pre1 = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            cur = max(pre1, pre2+ nums[i])
            pre2 = pre1
            pre1 = cur
        return pre1


if __name__ == "__main__":
    s = Solution()
    print(s.rob([8,1,2,9,6])) 
    print(s.rob1([8,1,2,9,6])) 
