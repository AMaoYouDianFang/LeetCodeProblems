
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
  
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head ==None: return head
        n=0
        cur1 = head
        while cur1:  #n=leng -1
            n += 1
            cur1 = cur1.next
        m = n // 2 + 1

        cur1 = head
        for i in range(m-1):
            cur1 = cur1.next  #移动到第1部分开始的结束
        head2 = cur1.next
        cur1.next = None
        cur2 = head2
       
        pre = None
        while cur2:
            nxt = cur2.next
            cur2.next = pre
            pre = cur2
            cur2 = nxt
        hea2 =pre
        cur2 = pre
        cur1 = head

        if cur2:
            while cur2.next:
                nxt1 = cur1.next
                nxt2 = cur2.next
                cur1.next = cur2
                cur2.next = nxt1
                cur1  = nxt1
                cur2  = nxt2
            tail = cur1.next if cur1.next else None
            cur1.next = cur2
            cur2.next = tail
        

   
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
    e=s.reorderList(res)
    s.listNodeToString(res)