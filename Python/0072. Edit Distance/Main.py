class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 and len(word2) == 0:  #bug
            return 0
        m = len(word1) +1  #miss 1
        n = len(word2) +1
        d = [[None] * n for i in range(m)]
        
        for i in range(m):
            d[i][0] = i
        for j in range(n):
            d[0][j] = j
        for i in range(1, m):
            for j in range(1,n):
                if word1[i-1] == word2[j - 1]:
                    d[i][j] = d[i-1][j-1]
                else:
                    d[i][j] = min(d[i-1][j-1],d[i-1][j],d[i][j-1]) + 1
        return d[m-1][n-1] 

if __name__ == "__main__":
    s = Solution()
    print(s.minDistance('','ba'))
    