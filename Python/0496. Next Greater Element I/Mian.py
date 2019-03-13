class Solution:
    def nextGreaterElement(self, nums1, nums2):
        dic = {}
        res = []
        for i in range(len(nums2)):
            dic[nums2[i]] = i
        for i in range(len(nums1)):
            start = dic[nums1[i]]
            res.append(-1)  #注意这里先赋值为1 ，再进修改
            for j in range(start+1, len(nums2)):
                if nums2[j] > nums1[i]:
                    res[i] = nums2[j]
                    break
    
        return res
                    

if __name__ == "__main__":
    s = Solution()
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    res = s.nextGreaterElement(nums1,nums2)
    print(res)