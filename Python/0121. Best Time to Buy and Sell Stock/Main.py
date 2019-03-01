#对于从第一天后的每一天i来说：

# 如果我们在第i天卖出，则能赚的钱是在第i-1卖能赚到的钱+（第i天的股价 - 第i-1的股价）
# 如果我们在第i天不卖出，则当前赚的钱为 0
# 所以对于第一天后的第i天来说，他能赚到的最多的钱就是上面两种情况中的较大值


class Solution:
    def maxProfit(self, prices):
        if not prices or len(prices) ==0:
            return 0
        opt = [0] *len(prices)
        for i in range(1,len(prices)): #注意从1开始
            opt[i] =max(opt[i-1]+prices[i]-prices[i-1], 0)
        return max(opt)