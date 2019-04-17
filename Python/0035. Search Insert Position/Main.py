class Solution:
    def searchInsert(self, nums, target):
        l = len(nums)
        for i in range(l):
            if nums[i] >= target:
                return i
        return l
    
    #二分法
    def searchInsert1(self, nums, target):
        r , l = 0 , len(nums) -1
        while r <= l:
            mid = (r + l) //2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l
 #解释键二分查找总结                   

if __name__ == "__main__":
    s=Solution()
    res =s.searchInsert([1,3,5,6],2)
    print(res)
             
