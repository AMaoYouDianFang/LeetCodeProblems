import sys
class Solution:
    def findMedianSortedArrays1(self, nums1, nums2):
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
        while (cut1 <= len(nums1)):  #cut1 从0 开始，到len(nums1)
            cut1 =  (cutR - cutL) // 2 + cutL
            cut2 = lng // 2 - cut1
            L1 = -sys.maxsize if cut1 == 0 else nums1[cut1-1]
            L2 = -sys.maxsize if cut2 == 0 else nums2[cut2-1] 
            R1 = sys.maxsize if cut1 == len(nums1) else nums1[cut1] 
            R2 = sys.maxsize if cut2 == len(nums2) else nums2[cut2] 
        #0 是不合法的位置
            if L1 >R2:
                cutR = cut1 -1
            elif L2 > R1:
                cutL = cut1 + 1  
            else:  #找到了切分点
                if lng %2 ==0: #一共偶数个元素
                    L1 = max(L1,L2)
                    R1 = min(R1,R2)
                    return (L1 + R1) / 2
                else:
                    print(R1,R2)
                    R1 = min(R1,R2) #总在这两个数中
                    return R1
        return -1



if __name__ == "__main__": 
    s= Solution()
    res = s.findMedianSortedArrays([1,2],[3,4])
    print(res)