# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
  
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        lst1 = []
        lst2 = []
        while l1:
            lst1.append(l1.val)
            l1 = l1.next
        while l2:
            lst2.append(l2.val)
            l2 = l2.next
        carry = 0 #表示进位
        head = None  #初始化不能是ListNode(None)
        while len(lst1) or len(lst2):
            x = lst1.pop() if len(lst1) else 0
            y = lst2.pop() if len(lst2) else 0
            s = carry + x + y
            carry = s // 10
            cur = ListNode(s % 10)
            cur.next = head
            head = cur
        if carry == 1:  #忘记
            cur = ListNode(1)
            cur.next = head
            head = cur
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
    res1= s.ToListNode([7,2,4,3])
    res2= s.ToListNode([5,6,4])
    e=s.addTwoNumbers(res1, res2)
    s.listNodeToString(e)
