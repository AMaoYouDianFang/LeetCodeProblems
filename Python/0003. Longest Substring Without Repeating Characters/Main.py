class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = [0] * 256 #ASCII 是256个
        i= 0
        j = 0
        maxLen = 0
        s = list(s)
        while i < len(s):
            while j <len(s):
                if count[ord(s[j])] > 0:
                    break
                count[ord(s[j])] += 1
                j += 1
            cur = j - i
            maxLen = max(maxLen, cur)
            count[ord(s[i])] -= 1
            i+= 1
        return maxLen

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring('abcabcbb'))

        