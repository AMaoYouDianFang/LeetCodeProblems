class Solution:
    def canJump(self, nums):
        n = len(nums)
        i= n - 2
        last = n - 1
        while i >=0:
            if nums[i] + i >= last:
                last = i
            i -= 1
        return last == 0 


# 从后往前判断，即从倒数第二个位置开始，以最大步数判断前面的位置能否跳到后面来，如果可以继续往前判断；
# 若最后能走到第一个位置，则说明从第一个位置也能走到最后。        