#解题思路：首先对数组进行排序，固定指针在第i个元素，然后利用twoSum对i+1 到end的元素进行求解，
#这里的twoSum 需要找出所有的组的解
class Solution:
    def threeSum(self, nums):
        res = set()
        for i in range(len(nums)):
            for j  in range(i+1, len(nums)):
                for k in range(j+ 1, len(nums)):
                    if nums[j] + nums[j] + nums[k] == 0:
                        res.add((nums[i], nums[j], nums[k]))
        return list(res)    
    

    

if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-1,0,1,2,-1,-4]))



# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         nums.sort()
        # N, result = len(nums), []
        # for i in range(N):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     target = nums[i]*-1
        #     s,e = i+1, N-1
        #     while s<e:
        #         if nums[s]+nums[e] == target:
        #             result.append([nums[i], nums[s], nums[e]])
        #             s = s+1
        #             while s<e and nums[s] == nums[s-1]:
        #                 s = s+1
        #         elif nums[s] + nums[e] < target:
        #             s = s+1
        #         else:
        #             e = e-1
        # return result