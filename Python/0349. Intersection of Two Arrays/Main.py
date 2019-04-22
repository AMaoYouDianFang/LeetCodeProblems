class Solution:
    def intersection(self, nums1, nums2) :
        res = []
        for i in nums1:
            if i in nums2:
                res.append(i)
        return set(res)


#利用二分法：思路是将一个数组排序，然后遍历另一个数组，把遍历到的每个数字在排序好
#的数组中用二分查找法搜索
    def intersection(self, nums1, nums2) :
        nums1 = set(nums1)
        res = []
        if nums1 == [] or nums2 == []: return res 
        nums2.sort() #需要先排序
        for i in nums1:
            if self.binarysearch(nums2,i) == True:
                res.append(i)
        return res
        
    def binarysearch (self, nums, target):
        s, e = 0, len(nums)-1
        while s <= e:
            mid = (s+e)//2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                s = mid + 1
            else:
                e = mid - 1
        return False
            


if __name__ == "__main__":
    s = Solution()
    print(s.intersection([1,2,3],[2,3,4]))