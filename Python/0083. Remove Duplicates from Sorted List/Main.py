# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
  
class Solution: 
    def deleteDuplicates(self, head):
        if not head:
            return None
        temp = head.val
        pre = head
        cur = head.next
        while cur != None:
            
            if cur.val == temp:
                cur = cur.next
                pre.next = cur
            else:
                temp = cur.val
                pre = pre.next
                cur =cur.next
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
    res= s.ToListNode([1,1,2])
    e=s.deleteDuplicates(res)
    s.listNodeToString(e)



        
