class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
  
class Solution:
    def splitListToParts(self, root, k):
        cur = root 
        l = 0
        res = []
        while cur:
            l += 1
            cur = cur.next
        avg = l //k
        ext = l % k
        for i in range(k):
            res.append(root)
            if root:  #要判断下
                for j in range(1,avg + (i < ext)):
                    root = root.next
                nxt = root.next
                root.next = None
                root = nxt
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
    res= s.ToListNode([1,2,3,4])
    e=s.splitListToParts(res,5)
    #s.listNodeToString(e)
