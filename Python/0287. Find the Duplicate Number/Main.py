# 2-14
class Solution(object):
    def findDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
    #快慢指针法
    def findDuplicate1(self, nums):
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = 0
        while True:
            fast = nums[fast]
            slow = nums[slow]
            if slow == fast:
                break  
        return slow  #!!注意不用nums[slow]
        
if __name__ == "__main__":
    s = Solution()
    nums = [2,5,9,6,9,3,8,9,7,1]
    res = s.findDuplicate1(nums)
    print(res)