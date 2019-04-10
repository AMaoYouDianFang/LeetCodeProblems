class Solution:
    def sortColors(self, nums):
        start = 0
        end = len(nums) - 1
        i = 0
        while i <= end:
            if nums[i] == 0:
                nums[i],nums[start] = nums[start],nums[i] #交换连个数
                start += 1
            elif nums[i] ==2:
                nums[i],nums[end] = nums[end],nums[i]
                end -= 1
                i-=1
            i+=1
        
if __name__ == "__main__":
    s = Solution()
    print(s.sortColors([2,0,2,1,1,0]))
            
        