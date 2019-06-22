class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inlst = []
        self.outlst = []

    def transform(self):
        if not self.outlst:
            while self.inlst:
                self.outlst.append(self.inlst.pop())
                
            
            
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inlst.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.transform()
        return self.outlst.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        self.transform()
        return self.outlst[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.inlst and not self.outlst:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()