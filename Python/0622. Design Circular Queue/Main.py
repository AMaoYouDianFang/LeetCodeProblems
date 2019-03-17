# http://www.cnblogs.com/grandyang/p/9899034.html
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.data = [0] * k
        self.size = k
        self.head = k - 1
        self.tail = 0
        self.cnt = 0  #当前队列中的数字个数
        #实际上head是指向数组范围内的起始位置的前一个数字，之所以初始化为 k-1，是因为起始时
        #我们假设数组的范围是 [0, k-1]，所以 0 的前一个不是 -1，而是 k-1，
        #因为是环形数组，同理，tail指向数组范围内的结束位置的下一个数字，k-1 的下一个位置不是k，
        #而是0
    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull(): return False
        self.data[self.tail] = value
        self.head = (self.tail + 1) % self.size
        self.cnt += 1
        return True



    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty(): return False
        
        self.head = (self.head + 1) % self.size
        self.cnt -= 1
        return True

        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        else: 
            return self.data[(self.head + 1 )% self.size] 

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        else: 
            return self.data[(self.tail - 1 + self.size)% self.size] 

        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.cnt == 0:
            return True
        else: 
            return False
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if self.cnt == self.size:
            return True
        else:
            return False
        
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
