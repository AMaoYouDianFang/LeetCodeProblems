from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = [False] * (len(s)+1)
        d[0] = True
        wordset = set(wordDict)
        for i in range(1,len(s)+1):
            for j in range(i-1, -1, -1):
                d[i] = d[j] and s[j:i] in wordset #不包括i
                if d[i] == True:
                    break
        return d[len(s)]

if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak("leetcode", ["leet","code"]))