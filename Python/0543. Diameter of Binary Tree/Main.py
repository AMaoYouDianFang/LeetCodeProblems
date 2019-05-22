#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        d = [0]
        self.maxDeep(root, d)
        return d[0] #注意
    
    def maxDeep(self, root, d):
        if not root: 
            return 0
        left = self.maxDeep(root.left,d)
        right = self.maxDeep(root.right,d)
        d[0] = max(d[0], left+right)
        return max(left, right) + 1

    def diameterOfBinaryTree1(self, root: TreeNode) -> int:
        if not root: return 0
        stack = []
        dic = {}
        stack.append(root)
        d = 0 #直径
        while stack:
            s = stack[-1]
            if s.left and s.left not in dic.keys():
                stack.append(s.left)
            elif s.right and s.right not in dic.keys():
                stack.append(s.right)
            else: #左右子节点是空，或者子节点的深度已经求出来
                stack.pop()
                left = dic[s.left] if s.left in dic.keys() else 0
                right = dic[s.right] if s.right in dic.keys() else 0
                d = max (d, left + right)
                dic[s] =  max(left, right) +1
        return d


