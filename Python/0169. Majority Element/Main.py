import collections
class Solution:
    def majorityElement(self, nums):
        d = {}
        for num in nums:
            d[num] = d.setdefault(num,0) +1
            # d[num] = d.get(num, 0) +1
        for key in d.keys():
            if d[key] > len(nums)//2:
                return key
        


if __name__ == "__main__":
    s = Solution()
    res = s.majorityElement([3,2,3])
    print(res)

