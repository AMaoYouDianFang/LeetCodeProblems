class Solution:
    def intersect(self, nums1, nums2):
        nums1.sort() #sort() 直接修改nums1
        nums2.sort()
        res = []
        l, r = 0,0
        while l < len(nums1) and r < len(nums2):
            if nums1[l] == nums2[r]:
                res.append(nums1[l])
                l += 1
                r += 1
            elif nums1[l] > nums2[r]:
                r += 1
            else:
                l += 1
        return res
        

        
if __name__ == "__main__":
    s = Solution()
    res = s.intersect([1,4,3],[4,3,2])
    print(res)
        