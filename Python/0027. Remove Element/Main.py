class Solution:
    def removeElement(self, nums, val):
        idx = 0
        while idx <len(nums):
            if nums[idx] ==val:
                nums[idx] = nums[-1]
                del nums[-1]
            else: idx += 1
        return idx

if __name__ == "__main__":
    s = Solution()
    res = s.removeElement([3,2,2,3],3)
    print(res)

