import math
class Solution:
    def numSquares(self, n: int) -> int:
        while n % 4 == 0:
            n = n // 4
        if (n % 8 == 7):
            return 4
        
        for a in range(n):
            b = (n - a * a) ** 0.5 #开平方
            if a**2 + b **2 == n:
                return (a>0) + (b>0)
        return 3
if __name__ == "__main__":
    s =Solution()
    res = s.numSquares(13)
    print(res)

