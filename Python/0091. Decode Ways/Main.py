class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or (len(s)>1 and s[0] =='0'):
            return 0  
        dp = [0] *(len(s) + 1)            
        for  i in range(len(dp)):
            dp[i] = 0 if s[i - 1] =='0' else dp[i-1]
            if (i>1 and (s[i-2] == '1' or s[i-2] == '2' and s[i-1]<= '6')):
                dp[i] += dp[i-2]
        return dp[-1]
# 代码有问题