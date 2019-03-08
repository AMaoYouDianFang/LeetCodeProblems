# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head : return None
        if not head.next:
            return TreeNode(head.val)
        slow = head
        fast = head
        last = slow
        while fast.next and fast.next.next:
            last = slow
            slow = slow.next
            fast = fast.next.next
        fast = slow.next  #第二部分链表头
        last.next = None  #第一部分链表尾
        cur = TreeNode(slow.val)
        if head != slow:
            cur.left = self.sortedListToBST(head)
        cur.right = self.sortedListToBST(fast)
        return cur
        
 