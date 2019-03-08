class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        stack = []
        cur = head
        while cur:
            if cur.child:
                cur.child.prev = cur
                if cur.next:
                    stack.append(cur.next)
                cur.next = cur.child
                cur.child = None
            else:
                if not cur.next:
                    if stack:
                        tmp = stack.pop()
                        cur.next = tmp
                        tmp.prev = cur
                    else:
                        return head
            cur = cur.next


