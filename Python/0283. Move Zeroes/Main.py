class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] =nums[i]
                j += 1
        print(j)
        print(nums[j:])
        while j < len(nums):
        	nums[j] = 0
        	j += 1
                
                
                
                

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    s =Solution()
    s.moveZeroes(nums)
    print(nums)