# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.dfs(root, 0)
        return root
    
    def dfs (self, root, sum):
        if not root: return sum
        root.val  += self.dfs(root.right, sum)
        return self.dfs(root.left, root.val)

    #迭代
    def convertBST(self, root: TreeNode) -> TreeNode:
        s = 0
        cur = root
        st = []
        while cur or st:
            while cur:
                st.append(cur)
                cur = cur.right
            t = st.pop()
            t.val += s
            s = t.val
            cur = t.left
        return root


        

        