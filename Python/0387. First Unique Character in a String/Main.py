class Solution:
    def firstUniqChar(self, s):
        cnt = [0] * 26
        for i in range(len(s)):
            cnt[ord(s[i]) - ord('a')] += 1
        for i in range(len(s)):
            if cnt[ord(s[i]) - ord('a')] == 1:
                return i
        return -1

if __name__ == "__main__":
    s= Solution()
    res = s.firstUniqChar("eetcode")
    print(res)