class Solution:
    def isValid(self, s: str) -> bool:
        dic = { ')' :'(', '}':'{', ']':'['}
        
        stack = []
        for c in s:
            if c in dic.values():
                stack.append(c)
            elif not stack:
                return False
            else:
                top = stack[-1]
                if top == dic[c]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False

if __name__ == "__main__":
    s = "()[]("
    print(Solution().isValid(s))

