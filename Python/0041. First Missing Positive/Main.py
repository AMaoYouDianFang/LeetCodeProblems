class Solution:
    def firstMissingPositive(self, nums):
        if not nums:
            return 1
        for i in range (1,len(nums)+2):
            if i not in nums:
                return i

if __name__ == "__main__":
    s= Solution()
    res = s.firstMissingPositive([3,2,1])
    print(res)

#https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/41_First-Missing-Positive