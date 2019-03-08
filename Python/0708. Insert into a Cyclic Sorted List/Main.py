class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insert(self, head, insertVal):
        if head == None:
            head = ListNode(0)
            head.next = head
            return head
        pre = head
        cur = pre.next
        while cur != head:
            if insertVal <=cur.val and insertVal >= pre.val:
                break
            if pre.val > cur.val and (pre.val <= insertVal or cur.val >= insertVal):
                break
            pre = cur
            cur = cur.next
        pre.next = ListNode(insertVal)
        pre.next.next = cur
        