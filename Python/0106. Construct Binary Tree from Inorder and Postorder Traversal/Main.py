class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        indic = { u : v for v, u in enumerate(inorder) }
        return self.helper(indic, postorder, 0, len(inorder)-1, 0, len(postorder)-1)
    
    def helper(self, indic, postorder, istart, iend, pstart, pend):
        if istart > iend: return None #pstart > pend 也可以
        roval = postorder[pend]
        idx = indic[roval]
        lng = idx - istart
        root = TreeNode(roval)
        root.left = self.helper(indic, postorder, istart, idx-1, pstart, pstart+ lng -1) 
        root.right = self.helper(indic, postorder, idx + 1, iend, pstart+ lng, pend-1)
        return root