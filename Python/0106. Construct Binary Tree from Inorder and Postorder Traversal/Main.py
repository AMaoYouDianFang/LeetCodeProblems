class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        return self.helper(inorder, 0 , len(inorder)-1, postorder, 0, len(postorder)-1)
    def helper(self, inorder, ileft, iright, postoder, pleft, pright):
        if ileft>iright or pleft > pright:  #终止条件不太明白
            return None
        cur = TreeNode(postoder[pright])

        for i in range(ileft, iright+1):
            if inorder[i] == cur.val:
                break
        cur.left = self.helper(inorder, ileft, i-1, postoder, pleft, pleft + i - ileft -1)
        cur.right = self.helper(inorder, i+1, iright, postoder, pleft +i -ileft, pright -1 )
        return cur

        
