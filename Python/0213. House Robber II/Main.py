class Solution:
    def helper(self, nums, start, end) :
        #用前题的写法会报错 测试用例（0,0）
        pre2 = 0
        pre1 = 0
        for i in range(start, end+1):
            cur = max(pre1, pre2+ nums[i])
            pre2 = pre1
            pre1 = cur
        return pre1
    
    def rob(self, nums) -> int:
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0] 
        n = len(nums)
        return max(self.helper(nums,0, n-2), self.helper(nums,1,n-1))


if __name__ == "__main__":
    s = Solution()
    print(s.rob([8,1,2,9])) 
    
        