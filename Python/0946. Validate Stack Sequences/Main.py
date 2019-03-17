class Solution(object):
    def validateStackSequences(self, pushed, popped):
        stack = []
        l = len(popped)
        k = 0
        for i in range(l):
            if stack and stack[-1] == popped[i]:
                stack.pop()
            else:
                while k < l  and pushed[k] != popped[i]:
                    stack.append(pushed[k])
                    k += 1
                k += 1
        return not stack
