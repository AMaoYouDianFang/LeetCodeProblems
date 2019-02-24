class Solution:
    def maxSubArrayLen(self, nums, k):

        res, sums = 0, 0
        d = {} #主键是前缀和，值是索引
        for i, num in enumerate(nums):
            sums += num
            if sums - k in d:
                res = max(res, i-d[sums-k])
            else:
                d[sums] = i
        return res

if __name__ == "__main__":
    s = Solution()
    res = s.maxSubArrayLen([1, -1, 5, -2, 3],3)
    print(res)