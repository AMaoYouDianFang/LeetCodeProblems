# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
  
class Solution:
    def removeElements(self, head, val):
        if not head: return None
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next!= None:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
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
    res= s.ToListNode([1,2,3,4,5])
    e=s.removeElements(res, 1)
    s.listNodeToString(e)