# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
  
class Solution:
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next =head
        cur = head
        while cur.next:
            if cur.val > cur.next.val:
                pre = dummy
                while cur.next.val > pre.next.val:
                    pre = pre.next
                tmp = cur.next.next
                prenxt = pre.next
                pre.next = cur.next
                cur.next = tmp
                pre.next.next = prenxt
            else:
                cur = cur.next
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
    res= s.ToListNode([1,3,2,5,4,6])
    e = s.insertionSortList(res)
    s.listNodeToString(e)