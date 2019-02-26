import sys
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        
        j = -1
        k = -1
        res = sys.maxsize
        for i, word in enumerate(words):
            if word == word1:
                j = i
            if word == word2:
                k = i
            if k != -1 and j!=-1:   #这个没有判断
                res = min(res, abs(j-k))
        return res

if __name__ == "__main__":
    word = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = 'coding'
    word2 = 'practice'
    s= Solution()
    res = s.shortestDistance(word,word1,word2)
    print(res)
            