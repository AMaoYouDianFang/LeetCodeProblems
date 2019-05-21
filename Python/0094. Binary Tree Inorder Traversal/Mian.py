from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        left.append(root.val)
        left.extend(right)
        return left
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack = []
        #stack.append(root)
        res = []
        while  root or stack: #一开始的root： while root
            while(root):
                stack.append(root)
                root = root.left
                #结束时root = NULL
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

