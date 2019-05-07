class Solution:
    #递归,复杂度高
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
    #迭代法
    def climbStairs1(self, n: int) -> int:
        first, second = 1, 1
        for i in range(n-1):  #bug
            third = first + second
            first = second
            second = third
        return second

if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(5))
    print(s.climbStairs1(5))