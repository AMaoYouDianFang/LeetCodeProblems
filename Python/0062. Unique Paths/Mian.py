class Solution:
    #动态规划
    def uniquePaths(self, m: int, n: int) -> int:
        if m< 1 or n<1: #miss
             return 0
        d = [[None] * n for i in range(m)]
        for i in range(m):
            d[i][0] = 1
        for j in range(n):
            d[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                d[i][j] = d[i-1][j] + d[i][j-1]
        return d[m-1][n-1]
    
    #数学方法
    def uniquePaths1(self, m: int, n: int) -> int:
        if m< 1 or n<1: #miss
             return 0
        small = min(m-1,n-1)
        total = m+n-2
        result =1
        for i in range(small):
            result = result * (total-i)/(i+1)
        return int(result)



if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(3,2))
    print(s.uniquePaths1(3,2))
  