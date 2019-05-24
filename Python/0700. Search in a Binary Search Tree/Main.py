class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if  not root: return root
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        if root.val < val:
            return self.searchBST(root.right, val)

     def searchBST(self, root: TreeNode, val: int) -> TreeNode:
         while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else: 
                root = root.right
        

               