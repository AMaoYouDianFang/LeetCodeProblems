class Solution:
    def searchRange(self, nums, target):
        s = 0
        e = len(nums) -1
        while s<= e:
            if nums[s] == target and nums[e] ==target:
                return [s,e]
            if nums[s]!= target:
                s += 1
            if nums[e] != target:
                e -= 1
            print(s,e)
            
        return [-1,-1]

if __name__ == "__main__":
    s=Solution()
    res =s.searchRange([1],0)
    print(res)
             
