class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.dummy = Node(-1)
        self.size = 0
        

    def get(self, index: int) -> int:
        if index< 0 or index >= self.size:
            return -1
        cur  = self.dummy
        for i in range(index + 1):
            cur = cur.next
        return cur.val
        
    def addAtHead(self, val: int) -> None:
        cur = Node(val)
        cur.next = self.dummy.next
        self.dummy.next = cur
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        cur = self.dummy.next
        while cur.next:
            cur = cur.next
        cur.next = Node(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size: return
        cur  = self.dummy
        for i in range(index):
            cur = cur.next
        new = Node(val)
        new.next = cur.next
        cur.next = new
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.size or index<0: return
        pre  = self.dummy 
        cur = pre.next
        for i in range(index):
            pre = pre.next
            cur = cur.next
        pre.next = cur.next
        self.size -= 1

    def listNodeToString(self):
        node = self.dummy.next
        if not node:
            return "[]"
        result = ""
        while node:
            result += str(node.val) + ", "
            node = node.next
        print("[" + result[:-2] + "]")   
        


# Your MyLinkedList object will be instantiated and called as such:
linkedList = MyLinkedList()
linkedList.addAtHead(1)
linkedList.listNodeToString()
#inkedList.addAtTail(2)
#linkedList.listNodeToString()
linkedList.addAtIndex(1,2)  #链表变为1-> 2-> 3
linkedList.listNodeToString()
linkedList.get(1)            #返回2

#linkedList.deleteAtIndex(1);  #现在链表是1-> 3
#linkedList.listNodeToString()
print(linkedList.get(1))           #返回3