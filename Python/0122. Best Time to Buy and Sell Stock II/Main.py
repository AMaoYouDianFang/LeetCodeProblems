class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res

if __name__ == "__main__":
    s = Solution()
    res = s.maxProfit([1,2,3,4,5])
    print(res)

