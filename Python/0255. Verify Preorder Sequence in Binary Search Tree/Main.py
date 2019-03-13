# Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

# You may assume each number in the sequence is unique.

# Follow up:
# Could you do it using only constant space complexity?
import sys
class Solution:
    def verifyPreorder(self, preorder):
        low = - sys.maxsize
        stack = []
        for i in preorder:
            print('ww',i,low)
            if i < low:
                return False
            while stack and i > stack[-1]:
                low = stack.pop()
                print(low, i)
            stack.append(i)
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.verifyPreorder([5,2,1,3,6]))