# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
  
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        head1 = head.next
        l1 = head
        l2 = head1
        cur = head1.next
        while cur and cur.next:
            l1.next = cur
            l1 = l1.next
            l2.next = cur.next
            l2 = l2.next
            cur = cur.next.next
        l2.next =None   #注意这个地方
        self.listNodeToString(l2)
        if cur:
            l1.next = cur
            l1 = l1.next
        l1.next = head1
        return head
        
            

   
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
    res= s.ToListNode([1,2,3])
    e=s.oddEvenList(res)
    s.listNodeToString(e)

    #[1,2,3]