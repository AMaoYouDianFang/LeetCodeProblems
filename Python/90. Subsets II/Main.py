#For every number in nums, we add it to every i in res. Ex. [[]], 
# we add [] + [1] to res. The new res is [ [], [1] ]. 
# Then add [] + [2] and [1] + [2], the new res is [[],[1],[2],[1,2]].

#To void the duplicate, we check if i + [num] is already in res. 
# So the iterate solution for Subsets II is:


class Solution:
    def subsets(self, nums):
        res = [[]]
        nums.sort()
        for num  in nums:
             res.extend([tmp + [num]  for tmp in res if tmp + [num] not in res])
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1,2,2]))
