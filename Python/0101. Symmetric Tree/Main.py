# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #递归JISJjsjis
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helper(root.left, root.right)

    def helper(self, left, right):
        if not left and not right:
            return True
        if not left and right or left and not right or left.val != right.val:
            return False
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)
    #迭代
    def isSymmetric1(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        while(stack):
            s = stack.pop()
            t = stack.pop()
            if not s and not t:
                continue
            if not s or not t or s.val != t.val:
                return False
            stack.append(s.left)
            stack.append(t.right)
            stack.append(s.right)
            stack.append(t.left)
        return True

