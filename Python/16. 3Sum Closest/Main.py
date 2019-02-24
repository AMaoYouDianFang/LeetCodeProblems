class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        cloest = nums[0] + nums[1] +nums[2] #因为是排好顺序的，所以前三个的和最小
        for i in range(len(nums)):   #for i in nums:  i是那个数组的值, range(5) 不包括5
            j, k = i + 1, len(nums) - 1
            while j < k:
                #print(i,j,k)
                sum = nums[i] + nums[j] + nums[k]
                if  abs(target - sum) < abs (target - cloest):
                    cloest = sum
                if sum == target:
                    return target
                elif sum > target:
                    k -=1
                else:
                    j += 1
        return cloest

if __name__ == "__main__":
    solution = Solution()
    res = solution.threeSumClosest([-1, 2, 1, -4], 1)                 
    print(res)

