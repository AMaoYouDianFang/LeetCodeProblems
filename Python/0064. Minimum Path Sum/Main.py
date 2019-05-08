class Solution:
    def minPathSum(self, a) -> int:
        m, n = len(a), len(a[0])
        d = [[None] * n for i in range(m)]
        d[0][0] = a[0][0] #bug 没有单独写
        for j in range(1,n):
            d[0][j] = d[0][j-1] + a[0][j]
        for i in range(1,m):
            d[i][0] = d[i-1][0] + a[i][0]
        for i in range(1,m):
            for j in range(1,n):
                d[i][j] = min(d[i-1][j], d[i][j-1]) + a[i][j]
        return d[m-1][n-1] #bug
    
    def minPathSum1(self, a) -> int:
        m, n = len(a), len(a[0])
        d = [None] * n
        d[0] = a[0][0]
        for i in range(1,n):
            d[i] = d[i-1] + a[0][i]
        for i in range(1,m):
            d[0] += a[i][0]
            for j in range(1,n):
                d[j] = min(d[j-1],d[j]) + a[i][j]
        return d[n-1]
if __name__ == "__main__":
    s = Solution()
    print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
    print(s.minPathSum1([[1,3,1],[1,5,1],[4,2,1]]))