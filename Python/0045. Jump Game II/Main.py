class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums: return -1
        mx = 0
        n = len(nums)
        d = [0] * n
        for i in range(n):
            if mx >= n -1 :
                return d[-1]
            if mx < i :
                return -1
            mx = max(mx, i+nums[i])
            lst = min(n-1, i+nums[i])
            j = lst
            while j > i and d[j] == 0:
                d[j] = d[i] + 1
                j -= 1
        return -1