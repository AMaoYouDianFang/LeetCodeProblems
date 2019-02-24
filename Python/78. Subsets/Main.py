
class Solution:
    def subsets(self, nums):
        res = [[]]
        
        for num  in nums:
             res.extend([tmp + [num]  for tmp in res])
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.subsets([3,2,1]))
