class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        dic  = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000}
        for i in range(len(s)):
            val = dic[s[i]]
            if i == len(s) - 1 or dic[s[i+1]] <= dic[s[i]]:
                res += dic[s[i]]
            else:
                res -= dic[s[i]]
        return res
