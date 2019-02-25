# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         d = {}
#         for i, num in enumerate(nums):
#             if target - num in d:
#                 return [d[target-num],i]
#             d[num] = i
#         #in 判断键是否存在于字典中
#         #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，
#         #seasons = ['Spring', 'Summer', 'Fall', 'Winter']
#         #list(enumerate(seasons))
#         #[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
#         #list(enumerate(seasons, start=1))       # 下标从 1 开始
#         #[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

# if __name__ == "__main__":
#     solution = Solution()
#     print(solution.twoSum([2,7,9,11],9))
    
class Solution:
    def twoSum(self, nums, target):
        d = {}
        for  i, num in enumerate(nums): #没有记住
            res = target - num
            if res in d:
                return [d[res],i]
            d[num] = i         #写错了

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2,7,4,5],3))