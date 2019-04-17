#2/8 
class Solution:
    def myPow(self, x: float, n: int) -> float:
        res  = 1
        i = abs(n) 
        while i != 0:
            if i % 2 == 1:
                res = res * x
            x = x * x
            i = i // 2
        return res if n >=0 else 1/res
       
if __name__ == "__main__":
    s = Solution()
    res = s.myPow(2.0, 10)