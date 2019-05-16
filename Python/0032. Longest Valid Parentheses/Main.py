class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stark = [-1]
        lst = list(s)
        maxLen = 0
        for i in range(len(lst)):
            if stark[-1] != -1 and lst[stark[-1]] == '(' and lst[i] == ')':
                stark.pop()
                curLen = i - stark[-1]
                maxLen = max(curLen, maxLen)
            else:
                stark.append(i)
        return maxLen

        #动态规划
        

if __name__ == "__main__":
    s =Solution()
    print(s.longestValidParentheses('()()))'))
        