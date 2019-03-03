class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        nums1.extend(nums2)
        nums1.sort()
        l = m + n
        if l%2 == 1:
            return nums1[l//2]
        else:
            return (nums1[l//2] + nums1[l//2-1]) / 2
    """
    最小的时间复杂度: Olog(min(m,n))
    index  0    1   2   3   4   5
    nums1  3    5   8   9
    nums2  1    2   7   10  11  12

    res    1    2   3   5   7 | 8   9   10  11  12
    """

    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):  #保证nums1长度小，减少遍历次数
            return self.findMedianSortedArrays(nums2, nums1) 
        lng = len(nums1) + len(nums2)
        cut1 = 0 #num1 切左边有几个元素
        cut2 = 0
        cutL = 0  #在nums1中二分法（cutL, cutR）
        cutR = len(nums1)
        while (cut1 <= len(nums1)):
            cut1 = 



if __name__ == "__main__": 
    s= Solution()
    res = s.findMedianSortedArrays([1,3],[2])
    print(res)