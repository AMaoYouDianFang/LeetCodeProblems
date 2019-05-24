# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        return self.helper(nums, 0, len(nums)-1)

    def helper(self, nums, s, e):
        if start > end: return None #注意
        mid = (s + e) // 2
        root  = TreeNode(nums[mid])
        root.left = self.helper( nums, s, mid-1 )
        root.right = self.helper(nums, mid+1, e)
        return root

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
