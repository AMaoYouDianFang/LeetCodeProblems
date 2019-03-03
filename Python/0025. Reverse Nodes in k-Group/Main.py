# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
  
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head == None or head.next == None:
            return head
        count = 0
        cur = head
        while cur != None and count != k:
            cur = cur.next
            count += 1 
        if count == k:  # 如果当前 k-group 有 k 个node的话 # 先找到第k个node之后的递归结果 node = nxt
                                             # 让反转结果的结尾 tail.next = nxt
            cur = self.reverseKGroup(cur,k)
            while count > 0:           # 反转前面k个node
                temp = head.next
                head.next = cur
                cur =head
                head = temp
                count -= 1
              #当前 k-group 压根没有k个node，那么我们直接保持这个k-group不动返回head
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
    res= s.ToListNode([1,2,3,4,5])
    e=s.reverseKGroup(res, 2)
    s.listNodeToString(e)
