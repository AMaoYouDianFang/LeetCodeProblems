# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    #递归方法
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p and q or p and not q or p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)

    #使用栈
    def isSameTree1(self, p: TreeNode, q: TreeNode) -> bool:
        stack = []
        stack.append(p)
        stack.append(q)
        while stack: #空节点（叶子）也会进入栈中
            s = stack.pop()
            t = stack.pop()
            if not s and not t: continue 
            if not s or not t: return False
            if s.val != t.val:
                return False
            stack.append(s.right)
            stack.append(t.right)
            stack.append(s.left)
            stack.append(t.left)
        return True


 