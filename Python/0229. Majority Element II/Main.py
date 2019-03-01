import collections
class Solution:
    def majorityElement(self, nums):
        d = {}
        res = []
        for num in nums:
            d[num] = d.setdefault(num,0) +1
        for key in d.keys():
            if d[key] > len(nums)//3:
                res.append(key)
        return res
        


if __name__ == "__main__":
    s = Solution()
    res = s.majorityElement([3,2,3])
    print(res)

