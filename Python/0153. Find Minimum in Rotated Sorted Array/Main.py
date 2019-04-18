#2-12
class Solution:
    def findMin(self, nums) -> int:
        s = 0
        e = len(nums) - 1
        while s < e:
            m = (s+e)//2
            if nums[m] > nums[e]:  #这里nums[end]作为目标target
                s = m + 1
            else:
                e = m 
        return nums[s]

if __name__ == "__main__":
    s = Solution()
    res = s.findMin([3,4,5,1,2])
    print(res)