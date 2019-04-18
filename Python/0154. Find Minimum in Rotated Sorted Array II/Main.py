class Solution:
    def findMin(self, nums) -> int:
        s = 0
        e = len(nums) - 1
        while s < e:
            m = (s+ e) // 2
            if nums[m] > nums[e]:
                s = m + 1
            elif nums[m] < nums[e]:
                e = m
            else:
                e -= 1
        return nums[s]

if __name__ == "__main__":
    s = Solution()
    res = s.findMin([2,0,2,2,2,2,2])
    print(res)