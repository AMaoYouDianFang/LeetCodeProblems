class Solution:
    def reverseWords(self, s: str) -> str:
        if not s or len(s) == 0:
            return s
        start = 0
        end = 0
        lst = list(s)
        n = len(lst)
        while start < n:
            while end < n and lst[end] != ' ':
                end += 1
            i = start
            j = end -1
            while i < j:
                temp = lst[j]
                lst[j] = lst[i]
                lst[i] = temp
                i += 1
                j -= 1
            start = end + 1
            end = start
        return "".join(lst)

if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords('i love you.'))