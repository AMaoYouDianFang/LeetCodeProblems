class Solution:
     def longestConsecutive(self, nums):
         nums = set(nums) #去除重复元素 set' object does not support index不能nums[i]
         length = 0
         for num in nums:
             if num - 1 not in nums: #不用对该元素进行判断
                 y = num + 1
                 while y in nums:
                     y += 1
                 length = max(length, y - num)
         return length
if __name__ == "__main__":
    s = Solution()
    res = s.longestConsecutive([100, 4, 200, 1, 3, 2])
    print(res)
                 
# 首先去重复，时间O(N),然后将所有元素都放到一个字典中，这样判断一个数字的后续在不在这个字典中，如果存在就一直判断下去，每次判断只要O(1)。

# 对于每个数，如果他的前续已经判断过了，他就没有必要判断了，继续判断下一个数，即：

# if num - 1 in nums:
#     continue