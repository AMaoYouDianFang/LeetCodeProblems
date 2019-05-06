class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        d = [[False] * l for i in range(l)]
        maxlen = 0
        start = 0

        for i in range(l-1, -1, -1):
            for j in range(i, l):
                if i == j:
                    d[i][j] = True
                elif i+ 1 == j:
                    d[i][j] = s[i] ==s[j]
                else:
                    d[i][j] = s[i] == s[j] and d[i+1][j-1]
                if d[i][j] and (j - i + 1 > maxlen):
                    maxlen = j - i + 1
                    start = i
        return s[start: start + maxlen] #mistake 不包括最后一位

    '''
    方法2
    '''
    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            right += 1
            left -= 1
        return right - left - 1  #wrong (right-1) - (left+1) + 1

    def longestPalindrome1(self, s: str) -> str:
        if s is None or len(s) ==0: return ''  #miss
        maxLen = 0
        for i in range(len(s)):
            l1 = self.helper(s,i,i)
            l2 = self.helper(s,i,i+1)
            l = max(l1, l2)
            if l > maxLen:
                maxLen = l
                strat = i - (l - 1) // 2
        return s[strat:strat + maxLen] 
        


            

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome('abcbab'))
    print(s.longestPalindrome1('abcbab'))