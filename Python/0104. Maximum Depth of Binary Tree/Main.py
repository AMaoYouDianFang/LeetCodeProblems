# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.right),self.maxDepth(root.left)) + 1

    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        stack = []
        stack.append(root)
        deep = 0  #是0 和111题不一样
        while stack:
            l = len(stack)
            for i in range(l):
                s = stack.pop(0)
                if s.left:
                    stack.append(s.left)
                if s.right:
                    stack.append(s.right)
            deep += 1
        return deep

