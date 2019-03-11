class Solution:
    def evalRPN(self, tokens):
        label = ['+', '-', '*', '/']
        stack = []
        for c in tokens:
            if c in label:
                num2 = stack.pop()
                num1 = stack.pop()
                if c == '+':
                    stack.append(num1 + num2)
                elif c == '-':
                    stack.append(num1 - num2)
                elif c == '*':
                    stack.append(num1 * num2)
                else:
                    # here take care of the case like "1/-22",
                    # in Python 2.x, it returns -1, while in 
                    # Leetcode it should return 0
                    if num1 * num2 < 0 and num1 % num2 != 0:
                        stack.append(num1 / num2 + 1)
                    else:
                        stack.append(num1 / num2)
            else:
                stack.append(int(c))
        return stack[-1]

if __name__ == "__main__":
    s = Solution()
    l = ["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]
    res = s.evalRPN(l)
    print(-4//4.1)