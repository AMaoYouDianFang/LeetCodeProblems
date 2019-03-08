# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#问题分析 
# 将G的元素放入Set，遍历head，若遇到一个元素在Set中并且下一个元素为空或者不在Set中，则将 
# 连通组件个数增1  
class Solution:
    def numComponents(self, head, G):
        res = 0
        while head:
            if head.val in G and ( head.next == None or head.next.val not in G):
                res += 1
            head = head.next
        return res
        

   
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
    e=
    s.listNodeToString(e)
