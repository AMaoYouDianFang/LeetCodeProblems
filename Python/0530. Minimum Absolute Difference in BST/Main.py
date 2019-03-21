# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def getMinimumDifference(self, root: TreeNode) -> int:
    
        lst = [sys.maxsize]
        res = self.inorder(root, -1, lst)
        return res

    def inorder(self, root, pre, lst):
        if not root:
            return 
        self.inorder(root.left, pre, lst)
        if pre != -1:
            lst[-1] = min(lst[-1], root.val - pre)
        pre = root.val
        self.inorder(root.right, pre, lst[-1])
 
