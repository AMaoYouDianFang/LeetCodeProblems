# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        if not root.left and not root.right:
            return root.val == sum
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
    # 迭代
    def hasPathSum1(self, root: TreeNode, sum: int) -> bool:   
        if not root: return False
        stack = []
        sumStack = []
        stack.append(root)
        sumStack.append(sum)
        while stack:
            n = stack.pop()
            s = sumStack.pop()
            if not n.left and not n.right and n.val == s:
                return True
            if n.left:
                stack.append(n.left)
                sumStack.append(s - n.val)
            if n.right:
                stack.append(n.right)
                sumStack.append(s - n.val)
        return False

            
