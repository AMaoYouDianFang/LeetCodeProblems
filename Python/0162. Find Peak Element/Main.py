
class Solution:
    def findPeakElement(self, nums):
        s = 0
        e = len(nums) - 1
        while s < e:  # 结束条件s==e
            mid = (s + e) // 2
            if nums[mid] < nums[mid + 1]:
                s = mid + 1
            elif nums[mid] > nums[mid + 1]:
                e = mid
        return s


if __name__ == "__main__":
    s = Solution()
    res = s.findPeakElement([1, 2, 3, 1])
    print(res)
