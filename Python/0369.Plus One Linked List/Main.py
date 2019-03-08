# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
  
class Solution:
    def plusOne(self, head):
        tmp = self.reverseLink(head)
        cur = tmp
        carry = 1
        while cur:
            pre = cur
            cur.val += carry
            carry = cur.val // 10
            print(cur.val)
            cur.val = cur.val % 10
            cur = cur.next
        if carry == 1:
            pre.next =ListNode(1)
        return self.reverseLink(tmp)

    
    def reverseLink(self, head):
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre


   
    def ToListNode(self, nums):
        dummyRoot = ListNode(0)
        ptr = dummyRoot
        for number in nums:
            ptr.next = ListNode(number)
            ptr = ptr.next
        ptr = dummyRoot.next
        return ptr

    def listNodeToString(self,node):
        if not node:
            return "[]"
        result = ""
        while node:
            result += str(node.val) + ", "
            node = node.next
        print("[" + result[:-2] + "]")   

if __name__ == "__main__":
    s = Solution()
    res= s.ToListNode([9,9,9,9])
    e=s.plusOne(res)
    s.listNodeToString(e)
