class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        res = []
        self.preor(root, res)
        return res
    
    def preor(self, root, res):
        if not root: return 
        res.append(root.val)
        self.preor(root.left,res)
        self.preor(root.right,res)

    #迭代
    def preorderTraversal(self, root):
        res = []
        tree = []
        if not root : return res
        tree.append(root)
        while tree:
            s = tree.pop()
            res.append(s.val)
            if s.right: 
                tree.append(s.right)
            if s.left:
                tree.append(s.left)
        return res
        
    
    


     