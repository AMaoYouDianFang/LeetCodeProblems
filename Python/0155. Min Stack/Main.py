class MinStack:
    
    def __init__(self):
        self.s1 = []
        self.s2 = []
        """
        initialize your data structure here.
        """
        

    def push(self, x: int):
        self.s1.append(x)
        if self.s2 ==[] or x <= self.s2[-1]:  #注意是《=
            self.s2.append(x)
        

    def pop(self):
        if self.s1[-1] == self.s2[-1]:
            self.s2.pop()
        self.s1.pop()
        

    def top(self):
        return self.s1[-1]
        

    def getMin(self) :
        return self.s2[-1]

if __name__ == '__main__':
    s = MinStack()
    