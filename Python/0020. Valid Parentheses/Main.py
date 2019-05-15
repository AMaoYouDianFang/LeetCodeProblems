class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')', '{':'}', '[' :']'} 
        stack = []
        for i in range(len(s)):
            if s[i] in dic.keys():
                stack.append(s[i])
            elif len(stack) == 0:  #忘了
                return False
            else:
                if s[i] == dic[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return True if len(stack)==0 else False

if __name__ == "__main__":
    s = "(])"
    print(Solution().isValid(s))
    #print(s[0])

