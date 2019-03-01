class Solution(object):
    def sortColors(self, nums):
        n = len(nums)
        red  =0
        blue = n -1
        i= 0

        while i<= blue:  #等于号》》》
            if nums[i] == 0:
                nums[i], nums[red] = nums[red], nums[i]
                red += 1
            elif nums[i] ==2:
                nums[i], nums[blue] = nums[blue], nums[i] #后面的交换到前面需要回退,重新判断
                blue -=1
                i -= 1
            i+=1

            print(nums)

           

if __name__ == "__main__":
    s =Solution()
    nums= [2,0,1]
    s.sortColors(nums)
    #print(nums)