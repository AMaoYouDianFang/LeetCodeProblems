#Definition for singly-linked list with a random pointer.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

# 两次遍历链表；

# 第一次：遍历的同时生成新结点，并建立一个原结点与新结点的哈希表；
# 第二次：查找哈希表给结点上的随机指针赋值。
# 使用字典实现哈希表。

#因为在第一次创建节点的时候，random可能指向未创建的节点
class Solution(object):
    def copyRandomList(self, head):
        #新链表 pre 是新链表的虚拟头节点
        pre = Node(-1,None,None)
        tail = pre
        d = {}

        #第一次遍历，建立新链表
        oldNode = head
        while oldNode:
            newNode = Node(oldNode.val,None,None)
            d[oldNode] = newNode  #把新的节点和原始的节点放入dic
            tail.next = newNode
            tail = tail.next
            oldNode = oldNode.next
        
        #第二次遍历，赋值random指针
        tail = pre.next  #两个指针分别指向链表的头部
        oldNode = head
        while oldNode:
            if oldNode.random:
                tail.random = d[oldNode.random]
            oldNode = oldNode.next
            tail = tail.next

        return pre.next
