# 如果i是奇数，nums[i] >= nums[i - 1]
# 如果i是偶数，nums[i] <= nums[i - 1]
# 所以我们只要遍历一遍数组，把不符合的情况交换一下就行了。
# 具体来说，如果nums[i] > nums[i - 1]， 则交换以后肯定有nums[i] <= nums[i - 1]。
class Solution(object):
    def wiggleSort(self, nums):
        for i in range(1, len(nums)):
            if (i % 2 == 1 and nums[i] < nums[i-1]) or (i % 2 == 0 and nums[i] > nums[i-1]):
                nums[i] , nums[i-1] = nums[i-1], nums[i]

if __name__ == "__main__":
    s = Solution()
    nums  = [1, 5, 1, 1, 6, 4]
    s.wiggleSort(nums)
    print(nums)    

