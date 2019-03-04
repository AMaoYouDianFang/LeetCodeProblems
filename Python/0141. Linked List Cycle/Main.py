# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head == None or head.next==None:
           return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast == None or fast.next == None: #因为fast每次走两步，所以可能到end 或者到end.next,要分别处理
                return False
            slow = slow.next
            fast = fast.next.next
        return True

        