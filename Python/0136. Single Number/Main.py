class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #相同的数异或为0 0和然和数异或是1
        res = 0
        for i in range(len(nums)):
            res  = res ^ nums[i]
        return res
