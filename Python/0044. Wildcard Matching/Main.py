class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        dp = [([False] * (n+1)) for i  in range(m+1)]  
        #不能[[false] *2]*3 会浅拷贝
        dp[0][0] = True #s,p为null
       
        #s为空，p为连续的*
        for i in range(1,n+1):
            if p[i-1] == '*':
                dp[0][i] =dp[0][i-1]
        
        
        for i in range(1,m+1):
            for j  in range (1,n+1):
                if p[j-1] =='*': #因为从1开始的，而字符串要从0开始  
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = (s[i - 1] == p[j - 1] or p[j - 1] == '?') and dp[i - 1][j - 1] 
        
        return dp[m][n]
        



    
if __name__ == "__main__":
    s = Solution()
    s.isMatch('aa','a')