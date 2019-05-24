from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, properder: List[int], inorder: List[int]) -> TreeNode:
        inorderDic = {k: v for v, k in enumerate(inorder)}
        return self.helper(properder,inorderDic, 0, len(properder)-1, 0, len(inorder)-1)
    
    def helper(self, properder, inorderDic, preStart, preEnd, inStart, inEnd):
        if preStart > preEnd: return None #注意不要拉这个条件
        roval = properder[preStart]
        root = TreeNode(roval)
        idex = inorderDic[roval]
        lng = idex - inStart
        root.left = self.helper(properder, inorderDic, preStart+1, preStart+lng, inStart, idex-1)
        root.right = self.helper(properder, inorderDic, preStart+1+lng, preEnd, idex+1, inEnd)
        return root