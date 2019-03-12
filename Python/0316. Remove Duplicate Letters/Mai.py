import collections
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = collections.Counter(s)
        vist = dict.fromkeys(count.keys(),0)
        res = '0'
        for c in s:
            count[c] -= 1
            if vist[c] == 1: continue
            while count[res[-1]] > 0 and c < res[-1]:  #注意这里是while循环
                vist[res[-1]] = 0
                res = res[:-1]
            res = res + c
            vist[c] = 1
        return res[1:]

if __name__ == '__main__':
    s = Solution()
    res = s.removeDuplicateLetters("cbacdcbc")
    print(res)
    
