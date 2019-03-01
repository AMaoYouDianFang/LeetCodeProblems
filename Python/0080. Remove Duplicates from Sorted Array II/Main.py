class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        if len(nums)<=2:
            return len(nums)
        i = 0
        while i< len(nums)-2:  #注意不能用for循环，nums长度是在改变
            if nums[i] ==nums[i+1] ==nums[i+2]:
                nums.pop(i)
            else:
                i += 1

        return len(nums)

if __name__ == "__main__":
    s = Solution()
    res = s.removeDuplicates([1,1,1,2,2,3])
    print(res)
        