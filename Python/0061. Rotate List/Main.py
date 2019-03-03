# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
  
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None or k ==0 : return head  #k == 0 需要判断！！！+
        lst = []
        while head != None:
            lst.append(head)
            head = head.next
        k = k % len(lst)
        if k == 0:         ##需要判断！！！！
            return lst[0]
        lst[-k-1].next = None
        lst[-1].next = lst[0]
        return lst[-k]
   
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
    e=s.rotateRight(res, 0)
    s.listNodeToString(e)
