# nums[0] < nums[1] > nums[2] < nums[3]....

class Solution:
    def wiggleSort(self, nums):
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

#[::-1] 是将数组反转 
#[4,5,5,6]

if __name__ == "__main__":
    nums = [1, 5,2, 3, 6, 8]
    nums.sort()
    half = len(nums[::2])
    res = nums[:half][::-1]
    print(res)