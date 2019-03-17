#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode):
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            res.append(stack[-1])
            for i in range(len(stack)):
                node = stack[0]
                stack.remove(0)
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
        return res