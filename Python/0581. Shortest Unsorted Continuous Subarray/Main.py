from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortnum = sorted(nums)
        i = 0 
        j = len(nums)-1
        while i <len(nums) and nums[i] ==sortnum[i]  : #注意要把i <len(nums)放在前面
            i+= 1
        while j>=0 and nums[j] == sortnum[j] :
            j-=1
        return max(j-i+1,0)

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        m = -1 #为了保证结果为0
        n = 0
        mx = - sys.maxsize
        mi = sys.maxsize
        for i in range(len(nums)):
            mx = max(nums[i], mx)
            if nums[i] != mx:
                m = i
            j = len(nums) - i -1
            mi  = min(nums[j],mi)
            if nums[j] != mi:
                n = j
        return m - n +1


if __name__ == "__main__":
    s = Solution()
    print(s.findUnsortedSubarray([1,2,3,4]))
    