class Solution:
    def threeSumSmaller (slef, nums, target):
        nums = sorted(nums)
        res = 0
        for i in range(len(nums)):
            j, k =i+1, len(nums) -1
                    
            while j<k:
                sum = nums[i] +nums[j] +nums[k]
                if sum >= target:
                    k -= 1
                else:
                    res += k - j  #核心，画图看看
                    j += 1
        return res
    
if __name__ == "__main__":
     solution = Solution()
     res = solution.threeSumSmaller([-2,0,1,3],2)
     print(res)

