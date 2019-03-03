#https://www.youtube.com/watch?v=caf17w29B4s
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
  

   
class Solution:
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next != None and p.next.next != None:
            if p.next.val == p.next.next.val:
                sameval = p.next.val
                while p.next!= None and p.next.val == sameval: #注意第一个条件
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
    res= s.ToListNode([1,1])
    e=s.deleteDuplicates(res)
    s.listNodeToString(e)

