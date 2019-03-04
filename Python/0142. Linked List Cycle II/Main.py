class Solution(object):
    #def detectCycle(self, head):
        # dic = {}
        # i = 0
        # while head!= None:
        #     if head in dic.keys():
        #         return dic[head]
        #     else:
        #         dic[head] = i
        #         i += 1
        #         head = head.next
        # return None  
        
     def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return None
        fast = slow = head
        met = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
            else:
                return None
        while head != slow:
            slow = slow.next
            head = head.next
        return head
        
if __name__ == "__main__":
    dic = {}
    dic[1] = 1
    print(dic[1])