#乘积最大公共子序列
class Solution():
    def maxProduct(self, nums):
        maxdp = [nums[0]] *len(nums)
        mindp = [nums[0]] *len(nums)

        for i in range(1, len(nums)):
            maxdp[i] = max(mindp[i-1]*nums[i], maxdp[i-1]*nums[i], nums[i])
            mindp[i] = min(mindp[i-1]*nums[i], maxdp[i-1]*nums[i], nums[i])

        return max(maxdp)

if __name__ == "__main__":
    s=  Solution()
    print(s.maxProduct([2,3,-2,4]))
