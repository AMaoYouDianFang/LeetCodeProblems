class Solution:
    def simplifyPath(self, path: str) -> str:
        temp = ''
        stack = []
        res = ''
        for c in path:
            if  c !='/':
                temp += c
            elif c == '/'  and temp:
                if temp == '..' and stack:
                    stack.pop()
                elif temp != '..' and temp != '.' :
                    stack.append(temp)
                temp = ''
        if temp == '..' and stack:
            stack.pop()
        elif temp!='..' and temp!='.' and temp:
            stack.append(temp)
        if not stack:
            res = '/'
        else:
            for i in stack:
                res = res + '/' + i
        return res
    
if __name__ == "__main__":
    #path = "/a/./b/../../c/"
    #path = '/../'
    path = '/..'
    #path = '"/a//b////c/d//././/.."'
    s= Solution()
    print(s.simplifyPath(path))

            
                
