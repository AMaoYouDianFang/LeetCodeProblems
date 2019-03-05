# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
  
class Solution:
    def sortList(self, head):
        if not head or not head.next: return head
        dic = {}
        cur = head
        while cur:
            dic[cur] = cur.val
            cur = cur.next
        res = head1 = ListNode(0)
       
        for item in sorted(dic.items(), key = lambda item:item[1]):
            item[0].next = None
            res.next = item[0]
            res = res.next
             
        return head1.next
   
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
    res= s.ToListNode([4,2,1,3])
    e=s.sortList(res)
    s.listNodeToString(e)