class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #递归
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        tmp = root.right
        root.right = root.left
        root.left = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    #队列
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return root
        stack = []
        stack.append(root)
        while stack:
            s = stack.pop(0)
            tmp = s.left
            s.left = s.right
            s.right = tmp
            if s.left:
                stack.append(s.left)
            if s.right:
                stack.append(s.right)
        return root