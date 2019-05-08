class Solution():
    def maxProduct(self, nums):
        curMax, curMin, Max = nums[0], nums[0], nums[0]
        for i in range(1,len(nums)): #bug从1开始
            #错误，更新了curMax
            #curMax = max(nums[i], nums[i]* curMax, nums[i]*curMin)
            #curMin = min(nums[i], nums[i]* curMax, nums[i]*curMin)
            a = nums[i]* curMax
            b = nums[i]*curMin
            c = nums[i]
            curMax = max(a,b,c)
            curMin = min(a,b,c)
            Max = max(curMax, Max)
        return Max

if __name__ == "__main__":
    s=  Solution()
    print(s.maxProduct([-4,-3,-2]))
