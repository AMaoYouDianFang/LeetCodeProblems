class Solution(object):
    def deserialize(self, s):
        stack = []
        sign = 1 #标记数字的正负
        temp = None

        for c in s:
            if c == '-':
                sign = -1
            elif '0' <= c <='9':
                temp = (temp or 0)* 10 + int(c)
            elif c == '[':
                stack.append(NestedInteger())
            else: 
                if temp:
                    stack[-1].add(NestedInteger(temp * sign))
                    temp = None
                    sign = 1
                if c == ']':
                    top = stack.pop()
                    if stack:
                        stack[-1].add(top)
                    else: 
                        return top
        return NestedInteger((temp or 0) * sign)
            







