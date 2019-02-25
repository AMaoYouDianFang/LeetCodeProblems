# 从index为1的num开始看


# 把差值序列的正负看成 ‘上升沿’或‘下降沿’
#u 表示最后为上升沿的差值长度
#d 表示表示最后为下降沿的差值长度

# 如果比之前一个数字大的话，添加一个上升沿, u  = d + 1
# 如果比之前一个数字小的话，添加一个下降沿 d = u + 1
# 如果与之前一个数字相等的话，那么当前这个数字可以直接删除不要

# 长度为差值长度+1
class Solution:
    def wiggleMaxLength(self, nums):
        u, d = 0,0
        if not nums:  #忘记了
            return 0
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] > nums[i-1]:
                u = d + 1
            elif nums[i] < nums[i-1]:
                d = u + 1
        return max(u,d) + 1

if __name__ == "__main__":
    s = Solution()
    res = s.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])
    print(res)
