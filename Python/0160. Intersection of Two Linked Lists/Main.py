# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
  
class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        lA , lB = 0, 0
        curA ,curB = headA, headB
        while curA:
            lA += 1
            curA = curA.next
        while curB:
            lB += 1
            curB = curB.next
        if lA > lB:
            for i in range (lA - lB):
                headA = headA.next
        else:
            for i in range(lB - lA):
                headB = headB.next
        while headA:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None
   
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
    res= s.ToListNode([0,9,1,2,4])
    res1= s.ToListNode([3,2,4])
    e=s.getIntersectionNode(res,res1)
    