#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        d = [0]
        self.maxDeep(root, d)
        return d[0] #注意
    
    def maxDeep(self, root, d):
        if not root: 
            return 0
        left = self.maxDeep(root.left,d)
        right = self.maxDeep(root.right,d)
        d[0] = max(d[0], left+right)
        return max(left, right) + 1