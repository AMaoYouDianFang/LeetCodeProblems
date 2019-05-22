# Definition for a binary tree node.
import sys
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #nlogn
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        leftValid = not root.left or self.getMax(root.left) < root.val
        righValid = not root.right or self.getMin(root.right) > root.val
        if leftValid and righValid and self.isValidBST(root.left) and self.isValidBST(root.right):
            return True
        else:
            return False
    
    def getMax(self, root):
        while root.right:
            root = root.right
        return root.val
    def getMin(self, root):
        while root.left:
            root = root.left
        return root.val

    #o(n)
    def isValidBST(self, root: TreeNode) -> bool:
        return self.heleper(root, None, None)
    
    def heleper(self, root, lower, heigher):
        if not root: return True
        if  lower and root.val <= lower.val:
            return False
        if  heigher and root.val >= heigher.val:
            return False
        return self.heleper(root.left, lower, root) and self.heleper(root.right, root, heigher)

        