# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return []
        res = []
        cur_val = [root]
        count = 0
        while cur_val:
            temp = []
            nxt_val = []
            for node in cur_val:
                if count%2 == 0:
                    temp.append(node.val)
                else:
                    temp.insert(0,node.val)
                if node.left:
                    nxt_val.append(node.left)
                if node.right:
                    nxt_val.append(node.right)
            count += 1
            res.append(temp)
            cur_val = nxt_val
        return res
            
