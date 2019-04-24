class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p, q = 0, 0
        while p < len(s) and q < len(t):
            if s[p] == t[q]:
                p += 1
            q += 1
        if p ==len(s):
            return True
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    res = s.isSubsequence("axc","ahbgdc")
    print(res)

