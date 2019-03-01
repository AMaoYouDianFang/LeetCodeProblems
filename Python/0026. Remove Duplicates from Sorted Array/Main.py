class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i = 0
        while i < len(nums)-1:
            if nums[i] ==nums[i+1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)

if __name__ == "__main__":
    s =Solution()
    res = s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    print(res)