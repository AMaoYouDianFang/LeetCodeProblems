class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)  #没有考虑
        for i in range(k):
            nums.insert(0,nums.pop())
            #nums[0:0] = [nums.pop()] 注意括号？？？
        return nums

if __name__ == "__main__":
    s = Solution()
    res = s.rotate([1,2,3,4,5,6,7],8)
    print(res)