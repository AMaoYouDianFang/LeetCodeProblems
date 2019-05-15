import sys
class Solution:
    def myAtoi(self, str: str) -> int:
        if not str: return 0
        sign = 1
        res = 0
        i = 0
        l = len(str)
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        while i<l and str[i] ==' ':
            i += 1
        if i<l and (str[i]=='+' or str[i] =='-'):
            sign = 1 if str[i] =='+' else -1
            i += 1
        while i < l and str[i] >= '0' and str[i]<= '9':
            if (res > MAX_INT // 10) or (res == MAX_INT //10 and ord(str[i]) - ord('0')>7):
                return MAX_INT if sign == 1 else MIN_INT
            res= 10* res + (ord(str[i])-ord('0'))
            i +=1
        return res*sign

if __name__ == "__main__":
    s=Solution()
    res = s.myAtoi("2147483648")
    print(res)
