# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #方法1
    def flatten(self, root: TreeNode) -> None:
        cur = root
        while cur:
            if cur.left:
                p = cur.left
                while p.right:
                    p = p.right
                p.right  = cur.right
                cur.right = cur.left
                cur.left  = None
            cur = cur.right
    #方法2 二叉树前顺序遍历，然后新建一个树
 
