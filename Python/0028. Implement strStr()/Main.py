class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == None or needle == None:
            return -1
        m = len(haystack)
        n = len(needle)
        for i in range(m-n+1):
            j = 0
            k = i #第一个字符串的长度
            while j < n and k < m:
                if needle[j] == haystack[k]:
                    j += 1
                    k += 1
                else:
                    break
            if j == n: #j最后多加了
                return i
        return -1
            