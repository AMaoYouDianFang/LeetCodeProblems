class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        s_num = []
        s_str = []
        st = ''

        for c in s:
            if '0' <= c <= '9':
                num = 10 * num + int(c)
            elif c == '[':
                s_num.append(num)
                s_str.append(st)
                st = ''
                num = 0
            elif c == ']':
                topnum = s_num[-1]
                s_num.pop()
                s_str[-1] += st * topnum
                st = s_str[-1]
                s_str.pop()
            else:
                st += c
        return s_str[-1] if s_str else st 




                

if __name__ == "__main__":
   s = Solution()
   res = s.decodeString("100[leetcode]")
   print(res)