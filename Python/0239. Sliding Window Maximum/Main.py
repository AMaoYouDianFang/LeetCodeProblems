class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums and k == 0:   #注意[] 0的情况
            return [] 
        res = []
        for i in range(len(nums)-k+1):
            res.append(max(nums[i:i+k]))
        return res
if __name__ == "__main__":
    s = Solution()
    res = s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)
    print(res)