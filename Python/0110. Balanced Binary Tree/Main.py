# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #递归
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        if abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False
    

    def getHeight(self, root):
        if not root: return 0
        return max(self.getHeight(root.left), self.getHeight(root.right)) +1 
    
    #O(n)递归
    def isBalanced(self, root: TreeNode) -> bool:
        res = self.getHeightAndCheck(root)
        return False if res == -1 else True

    def getHeightAndCheck (self, root):
        if not root: return True
        left = self.getHeightAndCheck(root.left)
        if left == -1: return -1
        right = self.getHeightAndCheck(root.right)
        if right == -1: return -1
        
        if abs(left - right) >1: return -1
        return max(left, right) + 1   

        
