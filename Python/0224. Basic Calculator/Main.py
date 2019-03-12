class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res, num, sign = 0, 0, 1
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in '+-':
                res += sign * num
                num = 0
                sign = 1 if c == '+' else -1
            elif c == '(': # push the result first, then sign;
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1 # reset the sign and res for the value in the parenthesis
            elif c == ')': # use elif because there may have space in input s
                res += sign * num # temporary res in this parenthesis
                num = 0
                res *= stack.pop() # sign before the left parenthesis
                res += stack.pop() # res calculated before the left parenthesis
        return res if num == 0 else res + sign * num