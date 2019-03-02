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
        idx = len(nums) - 1
        i = 0
        while idx >0:         
            if nums[idx] > nums[idx - 1]:
                for  i in range(len(nums)-1, idx-1, -1):  #遍历从前向后做没有成功
                    if nums[idx-1] < nums[i]:
                        break
                print(i)
                nums[i], nums[idx-1] = nums[idx-1], nums[i]
                print(nums)
                
                break
            idx -= 1
        nums[idx:] = list(reversed(nums[idx:])) #反转要放到最后，因为不存在的画直接反转

if __name__ == "__main__":
    s = Solution()
    nums = [3,2,1]# 1　（2）　7　　4　　3　　1
    s.nextPermutation(nums)
    print(nums)

#代码优化
#http://www.cnblogs.com/grandyang/p/4428207.html