class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root :
            return []
        stack = [root]
        while stack:
            t = stack.pop()
            res.append(t.val)
            if t.right:
                stack.append(t.right)
            if t.left:
                stack.append(t.left)
        return res

     