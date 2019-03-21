
class Solution:
    def countSmaller(self, nums) :
        res = []
        temp = []
        for i in range(len(nums)-1,-1,-1):
            left = 0
            right = len(temp)
            while left < right:
                mid = left + (right - left)//2
                if temp[mid] >= nums[i]:
                    right = mid
                else:
                    left = mid +1
            res[i] = right
            temp.insert(right,nums[i])
        return res
