class Solution:
    def containsDuplicate(self, nums):
        if len(set(nums)) == len(nums): #第一个len忘了
            return False
        else:
            return True

if __name__ == "__main__":
    s = Solution()
    res = s.containsDuplicate([0])
    print(res)