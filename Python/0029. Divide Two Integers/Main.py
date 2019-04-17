class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0: return 0
        if (dividend == -2147483648 and divisor == -1): return 2147483647 #特殊情况、
        label = (dividend ^ divisor) >= 0  
        #用异或来计算是否符号相异, dividend ^ divisor大于等于0 是同号
        print(label)
        res = 0
        t = abs(dividend)
        d = abs(divisor)
        #print(t)
        for i in range (31, -1, -1):
            print(t)

            if (t >> i) >= d: #找出足够大的数2^n*divisor
                res = res + (1<<i) #一定加括号（找了好半天）
                t -= d <<i   #将被除数减去2^n*divisor        
        return res if label else -res




if __name__ == "__main__":
    s = Solution()
    res = s.divide(2147483647,1)
    print(res)