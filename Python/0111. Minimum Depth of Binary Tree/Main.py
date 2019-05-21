# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left and root.right:
            return self.minDepth(root.right) + 1
        if root.left and not root.right:
            return self.minDepth(root.left) +1
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) +1:

    def minDepth1(self, root: TreeNode) -> int:
        if not root: return 0
        stack = []
        stack.append(root)
        deep = 1
        while stack:
            l = len(stack)
            for i in range(l):
                s = stack.pop(0)
                if not s.left and not s.right:
                    return deep
                if s.right:
                    stack.append(s.right)
                if s.left:
                    stack.append(s.left)
            deep += 1
        return -1
                
