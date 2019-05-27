# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ppath = []
        qpath = []
        self.helper(root, p, ppath)
        self.helper(root, q, qpath)
        res = 0
        for i in range(min(len(ppath), len(qpath))):
            if ppath[i] == qpath[i]:
                res = i
        return ppath[res]
            
    
    def helper(self, root, p, path):
        if not root : return False  
        path.append(root)
        if root == p: return True
        ret = self.helper(root.left, p, path) or self.helper(root.right, p, path)
        if ret: return True
        else:
            path.pop()
            return False
    
        