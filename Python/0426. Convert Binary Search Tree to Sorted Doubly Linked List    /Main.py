class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def treeToDoublyList(self, root):
        if not root: return None
        head = None
        pre = None
        pre.right = head
        head.left = pre
        return head #最后首尾链接一起

    def inorder(self, node, pre, head):# 变量pre，来记录上一个遍历到的结点. 变量head，来记录最左结点
        if not node: return   #先判空，之后对左子结点调用递归
        inorder(node.left, pre, head) #这样会先一直递归到最左结点
        if not head:  #head为空的话, 当前就是最左结点，赋值给head和pre
            head = node
            pre = node
        else:
            pre.right = node
            node.left = pre
            pre = node
        inorder(node.right,pre, head)


        

