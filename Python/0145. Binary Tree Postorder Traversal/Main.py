# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode):
        if not root:
            return []
        res = []
        stack =[root]
        while stack:
            t = stack.pop()
            res.insert(0, t.val)
            if t.left: stack.append(t.left)
            if t.right: stack.append(t.right)
        return res