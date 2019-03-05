# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
  
class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        m = 0
        cur = head
        while cur:
            m+= 1
            cur = cur.next
        n = m // 2 + 1
        
        cur2 = head
        for i in range (n- 2):
            cur2 = cur2.next
        head2 = cur2.next
        cur2.next = None
        pre = None
        cur2 = head2
        while cur2:
            nxt = cur2.next
            cur2.next = pre
            pre = cur2
            cur2 = nxt
        head2 = pre
        self.listNodeToString(head)
        self.listNodeToString(head2)
        while head:
            if head.val != head2.val:
                return False
            else:
                head = head.next
                head2 = head2.next
        return True 


   
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
    res= s.ToListNode([1,0,1])
    e=s.isPalindrome(res)
    print(e)