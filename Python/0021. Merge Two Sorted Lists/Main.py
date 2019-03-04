# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
  
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p, q = l1, l2
        dummy = ListNode(0)
        cur = dummy
        while p and q:
            if p.val <q.val: 
                cur.next = p
                p = p.next
            else:
                cur.next = q
                q = q.next
            cur = cur.next
            
        if p: cur.next = p
        if q: cur.next = q
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
    res= s.ToListNode([1,2,4])
    res2 = s.ToListNode([1,3,4])
    e=s.mergeTwoLists(res, res2)
    s.listNodeToString(e)
