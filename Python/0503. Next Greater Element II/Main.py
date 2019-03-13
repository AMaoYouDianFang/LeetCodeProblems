class Solution:
    def nextGreaterElements(self, nums):
        res = [-1] * len(nums)
        for i in range(len(nums)):
            find = 0
            for j in range (i+1, len(nums)):
                if nums[j] >nums[i]:
                    res[i] = nums[j]
                    find = 1
                    break
            if find == 0:
                for j in range(0, i):
                    if nums[j] >nums[i]:
                        res[i] = nums[j]
                        break
        return res
if __name__ == "__main__":
    s = Solution()
    res = s.nextGreaterElements([1,2,1])
    print(res)