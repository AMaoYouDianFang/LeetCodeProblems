# Definition for a binary tree node.
import sys
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, -sys.maxsize, sys.maxsize)
    
    def helper(self, root, mn, mx):
        if not root:
            return True
        if root.val <= mn or root.val >=mx:
            return False
        return self.helper(root.left, mn, root.val) and self.helper(root.right, root.val, mx)
        