from typing import List
class Solution:
    #动态规划
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        l = len(nums)
        d = [1] *l
        maxLen = 1
        for i in range(1,l):
            for j in range(0,i):
                cur = d[j] + 1 if nums[i] > nums[j] else 1
                d[i] = max(d[i], cur)
            maxLen = max(maxLen, d[i])
        return maxLen
    
    def binarySearch (self, nums, lng, target):
        s, e = 0, lng-1
        while s <= e:
            mid = (s + e) // 2 
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                e = mid - 1
            else:
                s = mid + 1
        return s
    
    def lengthOfLIS1(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        l = len(nums)
        lng = 0
        d = [None] * len(nums)
        for num in nums:
            i = self.binarySearch(d,lng,num)
            d[i] = num
            if i == lng:
                lng += 1
        return lng

    



if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLIS([1,8,2,6,4,5]))
    #print(s.binarySearch([1,3,5,7],8))
    print(s.lengthOfLIS1([1,8,2,6,4,5]))