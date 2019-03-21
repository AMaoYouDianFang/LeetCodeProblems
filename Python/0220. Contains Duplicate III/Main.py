class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        dic = {}
        j = 0
        for i in range(len(nums)):
            if i - j >k 