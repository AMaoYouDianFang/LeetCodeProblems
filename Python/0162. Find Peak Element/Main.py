class Solution:
    def findPeakElement(self, nums): 
        for i in range(1, len(nums)):  #因为只需要返回任意一个
            if nums[i] < nums[i-1]:
                return i-1
        return len(nums) - 1 

if __name__ == "__main__":
    s = Solution()
    res = s.findPeakElement([1,2,3,1])
    print(res)