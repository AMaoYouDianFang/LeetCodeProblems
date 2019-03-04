# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
  
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head == None : return
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        for i in range(m-1):
            p = p.next

        first = p #第一段的最后一个
        sec = p.next  #第二段的最后一个
        pre = None
        p = p.next
     
        for j in range(n - m + 1): #写反了
            
            next = p.next
            p.next = pre
            pre = p
            p = next
        first.next = pre
        sec.next = p
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
    e=s.reverseBetween(res, 2,4)
    s.listNodeToString(e)