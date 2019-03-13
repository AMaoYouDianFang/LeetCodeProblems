 #Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode):
        if not root:
            return []
        res = []
        cur_level = [root]
        while cur_level:
            temp = []
            nxt_level = []
            for node in cur_level:
                temp.append(node.val)
                if node.left:
                    nxt_level.append(node.left)
                if node.right:
                    nxt_level.append(node.right)
            res.insert(0,temp)
            cur_level = nxt_level
        return res