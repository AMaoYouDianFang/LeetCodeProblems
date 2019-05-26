# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root : return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key) # root.left 注意
        elif root.val < key:
            root.right =  self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right #这里也写错了
            elif not root.right:
                return root.left
            else:
                temp = root.left
                while temp.right:
                    temp = temp.right
                temp.right = root.right
                root = root.left
        return root

