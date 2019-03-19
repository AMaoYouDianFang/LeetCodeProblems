# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findLeaves(self, root: TreeNode):
        res = [[]]
        self.helper(root, res)
        return res
    def helper(self, node, res):
        if not node: return -1 
        depth =  1 + max(self.getDepth(node.left), self.getDepth(node.right))
        if depth > len(res):
            res.append([])
        res[depth].append(node.val)
        return depth