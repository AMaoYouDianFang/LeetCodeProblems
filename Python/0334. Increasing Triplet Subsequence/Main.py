# 给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。
#递增不一是相差为1
import sys
class Solution:
    def increasingTriplet(self, nums):
        fmin, smin = sys.maxsize, sys.maxsize
        for i in nums:
            if i <= fmin: #注意等于号
                fmin =  i
                print('f',fmin)
            elif i <= smin:
                smin = i
                print('s' ,smin)
            else: 
                return True
        return False
if __name__ == "__main__":
    s = Solution()
    nums = [1,1,-2,6]
    res = s.increasingTriplet(nums)
    print(res)