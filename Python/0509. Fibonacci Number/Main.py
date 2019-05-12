class Solution:
    def fib(self, N: int) -> int:
        if N<= 0: return 0  #没有写
        if N == 1: return  1
        first = 0
        second = 1
        for i in range(2, N+1):
            cur = first + second
            first = second
            second = cur
        return second

if __name__ == "__main__":
    s = Solution()
    print(s.fib(3))