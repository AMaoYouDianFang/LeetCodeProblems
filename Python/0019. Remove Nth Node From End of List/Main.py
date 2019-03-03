# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
  
class Solution:
    def removeNthFromEnd(self, head, n):
        if not head:
            return None
        if n == 0:
            return head
        
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
        
        #删除第一个
        if fast == None:
            return head.next
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

#或者过加入头节点 利用一边循环的
#https://github.com/apachecn/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/0019._remove_nth_node_from_end_of_list.md
    def removeNthFromEnd1(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = fast = dummy = ListNode(-1)
        dummy.next = head
        for i in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
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
    res= s.ToListNode([1,2,3,4,5])
    e=s.removeNthFromEnd1(res, 2)
    s.listNodeToString(e)



        