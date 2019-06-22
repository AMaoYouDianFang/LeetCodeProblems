# 1　　2　　7　　4　　3　　1
# 下一个排列为：
# 1　　3　　1　　2　　4　　7

#可以发现，如果从末尾往前看，数字逐渐变大，到了2时才减小的，
#然后我们再从后往前找第一个比2大的数字，是3，那么我们交换2和3，再把此时3后面的所有数字转置一下
# 1　（2）　7　　4　　3　　1
# 1　（2）　7　　4　（3）　1
# 1　（3）　7　　4　（2）　1
# 1　　3　　1　　2　　4　　7

class Solution(object):
    def nextPermutation(self, nums):
        i = len(nums)-1
        p = len(nums) -1
        while i-1 >=  0 and nums[i-1] >= nums[i]:
            i -= 1
        
        if i > 0:
            n = nums[i-1]
            while nums[p] <= n:
                p -= 1
            nums[i-1], nums[p] = nums[p], nums[i-1]
        
        nums[i:] = list(reversed(nums[i:]))
         #反转要放到最后，因为不存在的画直接反转

if __name__ == "__main__":
    s = Solution()
    nums = [3,2,1]# 1　（2）　7　　4　　3　　1
    s.nextPermutation(nums)
    print(nums)

#代码优化
#http://www.cnblogs.com/grandyang/p/4428207.html