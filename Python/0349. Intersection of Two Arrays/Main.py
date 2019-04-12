class Solution:
    def intersection(self, nums1, nums2) :
        res = []
        for i in nums1:
            if i in nums2:
                res.append(i)
        return set(res)

if __name__ == "__main__":
    s = Solution()
    print(s.intersection([1,2,3],[2,3,4]))