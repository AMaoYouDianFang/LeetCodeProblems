# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
  
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q = l2
        dummy = ListNode(0)
        cur = dummy
        carry = 0 #表示进位
        while p or q:
            x = p.val if p else 0  #注意指针是p，q
            y = q.val if q else 0
            s = x + y + carry
            carry = s // 10
            s = s % 10
            cur.next = ListNode(s)
            cur = cur.next
            if p: p = p.next
            if q: q = q.next
        if carry == 1:
            cur.next = ListNode(1)
        return dummy.next



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
    res= s.ToListNode([2,4,3])
    res2 = s.ToListNode([5,6,4])
    e=s.addTwoNumbers(res, res2)
    s.listNodeToString(e)