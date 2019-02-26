class Solution:
    def maximumGap(self, nums):
        nums.sort()
        maxdif = 0
    
        for i in range(1, len(nums)):
            dif = nums[i] - nums[i-1] 
            maxdif = dif if dif > maxdif else maxdif
        return maxdif

if __name__ == "__main__":
    s = Solution()
    res =s.maximumGap([3,6,9,1])
    print(res)
