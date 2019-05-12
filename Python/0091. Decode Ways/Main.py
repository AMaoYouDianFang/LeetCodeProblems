class Solution:
    def isDigit(self, a, b): #条件写错了
        return a =='1' and b<='9' or a=='2' and b<='6'
    def numDecodings(self, s: str) -> int:
        l = len(s)
        d = [0] * (l+1)
        d[0] = 1
        d[1] = 1 if s[0] != '0' else 0
        for i in range(2, l+1):
            if  s[i-1] != '0':
                d[i] += d[i-1]
            if self.isDigit(s[i-2], s[i-1]):
                d[i] += d[i-2]
        return d[l] 

if __name__ == "__main__":
    s = Solution()
    print(s.numDecodings('226'))
