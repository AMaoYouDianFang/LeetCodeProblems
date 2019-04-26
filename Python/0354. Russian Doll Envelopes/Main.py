from typing import List
class Solution:
    #超出时间限制
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        res = 0
        dp = [1] * len(envelopes)
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1) 
            res = max(res,dp[i])
        return res