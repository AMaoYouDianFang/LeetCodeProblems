class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return False
        n = len(nums)
        mx = 0
        for i in range(n):
            if mx >= n -1:
                return True
            if mx < i:
                return False
            mx = max(mx, nums[i]+ i)
        return False
        