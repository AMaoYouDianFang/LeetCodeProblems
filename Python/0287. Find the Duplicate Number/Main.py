class Solution(object):
    def findDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
    
if __name__ == "__main__":
    s = Solution()
    nums = [3,1,3,4,2]
    res = s.findDuplicate(nums)
    print(res)