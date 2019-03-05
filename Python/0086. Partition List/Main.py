# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
  
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head == None: return 
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        lst2 = ListNode(0)
        cur2 = lst2
        while cur.next:
            if cur.next.val < x:
                cur = cur.next
            else:
                cur2.next = cur.next
                cur.next = cur.next.next
                cur2 = cur2.next
                cur2.next = None
        cur.next = lst2.next
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
    res= s.ToListNode([1,4,3,2,5,2])
    e=s.partition(res,3)
    s.listNodeToString(e)
