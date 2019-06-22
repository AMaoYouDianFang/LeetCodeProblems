#解题思路：首先对数组进行排序，固定指针在第i个元素，然后利用twoSum对i+1 到end的元素进行求解，
#这里的twoSum 需要找出所有的组的解
class Solution:
    #暴力
    def threeSum(self, nums):
        res = set()
        nums.sort() #需要排序
        for i in range(len(nums)):
            for j  in range(i+1, len(nums)):
                for k in range(j+ 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add((nums[i], nums[j], nums[k]))
        return list(res)

    #方法2
    def twoSum(self, nums, target):
        start = 0
        end = len(nums) - 1  #忘了减去1
        res = set()
        
        while(start < end):
            sum = nums[start] +nums[end]
            if sum > target :
                end -= 1
            elif sum < target:
                start +=1
            elif sum == target :
                res.add((nums[start],nums[end]))
                end -= 1
                start +=1
        #print(res)
        return res
        
    def threeSum(self, nums):
        nums = sorted(nums)
        res = set()
        for i in range (0, len(nums)-2):  
            target = -nums[i]
            twosum = self.twoSum(nums[i+1:],target)  # 类内函数调用加self数组的切片操作，切片操作
            if len(twosum):
                for j in twosum:
                    res.add((nums[i],j[0],j[1]))
        #print(list(res))
        return list(res)

    #合在一起的（algocast）

    

if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([0,0,0,0]))



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