class Solution:
    def numTrees(self, n: int) -> int:
        
        d = [0] * (n+1)
        d[0] = 1
        for i in range(1, n+1):
            for j in range(0,i):
                d[i] += d[j] * d[i-j-1]  #写错了，列举个3的例子

        return d[n]

if __name__ == "__main__":
    s = Solution()
    print(s.numTrees(3))