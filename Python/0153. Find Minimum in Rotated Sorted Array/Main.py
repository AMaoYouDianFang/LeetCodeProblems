#2-12
class Solution:
    def findMin(self, nums) -> int:
        s = 0
        e = len(nums) - 1
        while s < e:
            m = (s+e)//2
            if nums[m] > nums[e]: 
                s = m + 1
            else:
                e = m 
        return nums[s]
    
    def findMin1(self, nums) -> int:
        s = 0
        e = len(nums) - 1
        while s < e:
            if nums[s] < nums[e]: #提前结束
                return nums[s]
            m = (s+e)//2
            if nums[m] > nums[e]:  
                s = m + 1
            else:
                e = m 
        return nums[s]


if __name__ == "__main__":
    s = Solution()
    res = s.findMin([3,4,5,1,2])
    print(res)
