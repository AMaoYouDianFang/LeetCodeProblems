class Solution:
    def searchInsert(self, nums, target):
        if target not in nums:
            nums.append(target)
            nums.sort()
        for i in range(len(nums)):
            if nums[i] ==target:
                return i
                    

if __name__ == "__main__":
    s=Solution()
    res =s.searchInsert([1,3,5,6],2)
    print(res)
             
