from typing import List
class Solution:
    #T O(n) S O(n)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = [0] * len(nums)
        for i in range(len(nums)):
            n[nums[i]-1] += 1
        res = []
        for i in range(len(n)):
            if n[i] == 0:
                res.append(i+1)
        return res

if __name__ == "__main__":
    s =Solution()
    print(s.findDisappearedNumbers([1,2,2]))