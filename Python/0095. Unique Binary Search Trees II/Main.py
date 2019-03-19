# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int):
        if n == 0: return []
        return self.helper(1,n)
    
    def helper(self, start, end):
        subTree = []
        if (start > end):
            subTree.append(None)
        else:
            for i in range(start, end+1):
                leftSubTree = self.helper(start, i - 1)
                rightSubTree = self.helper(i+1, end)
                for j in range(len(leftSubTree)):
                    for k in range(len(rightSubTree)):
                        node = TreeNode(i)
                        node.left = leftSubTree[j]
                        node.right = rightSubTree[k]
                        subTree.append(node)
        return subTree

        