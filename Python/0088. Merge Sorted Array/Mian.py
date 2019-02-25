#由于两个数组都按升序排列，因此从后往前比较两个数组中的元素，将其中较大的一个插入nums1的末尾；
#若最后nums2中还有元素未插入nums1中，剩下的一定都比nums1中已放好的元素小，只需依次放进去就行。
class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = n + m -1
        while i>=0 and j>=0: #等于
            if nums1[i] >=nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else: 
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
        while j>=0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
        print(j)
        # print(k) 不对，不清楚为什么
        # if j>=0:
        #     nums1[:k] = nums2[:j]
        
if __name__ == "__main__":
    nums1 = [0]
    m = 0
    nums2 = [1]       
    n = 1
    s = Solution()
    s.merge(nums1,m,nums2,n)
    print(nums1)



