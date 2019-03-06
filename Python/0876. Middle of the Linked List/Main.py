# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
  
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        cur = head
        n = 0
        while cur:  #这样记录的是链表元素个数
            n += 1
            cur = cur.next
        for i in range(n//2 ):
            head = head.next
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
    res= s.ToListNode([1])
    e=s.middleNode(res)
    s.listNodeToString(e)
