class Solution:
    def minSubArrayLen(self, s, nums):
        l = len(nums) + 1 #+1是为了避免所有数的和小于k， 纠结好半天。。
        sums  = 0
        left = 0
        for i in range(len(nums)): #i 是right 
            sums += nums[i]           
            while sums >= s:
                sums -= nums[left]
                l = min(i - left + 1, l)
                left += 1
            
        return l if l <= len(nums) else 0

if __name__ == "__main__":
    s = Solution()
    res = s.minSubArrayLen(7,[2,3,1,2,4,3])
    print(res)

