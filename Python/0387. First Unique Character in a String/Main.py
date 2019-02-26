class Solution:
    def firstUniqChar(self, s):
        cnt = [0 for i in range(26)]
        for c in s:
            cnt[ord(c) - ord('a')] += 1

        for i, c in enumerate(s):
            if cnt[ord(c) - ord('a')] == 1:
                return i
        return -1   #忘记了

if __name__ == "__main__":
    s= Solution()
    res = s.firstUniqChar("leetcode")
    print(res)