import sys
class Solution:
    def maxProfit(self, prices):
        buy1 = sys.maxsize
        aftersell1 = 0
        afterbuy2 = -sys.maxsize-1 #注意取最小值
        aftersell2 = 0

        for i in range (len(prices)):
            # 第一次买入价格，越小越好
            buy1 = min(buy1, prices[i])
            #第一次卖出后获得的利润，越大越好
            aftersell1 = max(aftersell1, prices[i] - buy1)
            #/ 用第一次交易的利润做第二次买入后获得的利润，越大越好
            afterbuy2 = max(afterbuy2, aftersell1 - prices[i])
            # 第二次卖出后获得的利润，越大越好
            aftersell2 = max(aftersell2,afterbuy2 + prices[i])
        return aftersell2

if __name__ == "__main__":
    s =Solution()
    res = s.maxProfit([1,2,3,4,5])
    print(res)
