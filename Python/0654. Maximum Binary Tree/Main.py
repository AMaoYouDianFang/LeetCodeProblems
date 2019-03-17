# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums) -> TreeNode:
        if not nums:
            return None
        mx = nums[0]
        mx_id = 0
        for i in range(len(nums)):
            if nums[i] > mx:
                mx_id = i
                mx = nums[i]
      
        treeNode = TreeNode(mx)
        leftArr = nums[:mx_id]  #注意边界[ ）
        rightArr = nums[1+mx_id:]
        treeNode.left = self.constructMaximumBinaryTree(leftArr)
        treeNode.right = self.constructMaximumBinaryTree(rightArr)
        return treeNode

if __name__ == "__main__":
    s= Solution()
    s.constructMaximumBinaryTree([3,2,1,6,0,5])
