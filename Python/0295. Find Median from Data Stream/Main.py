import bisect
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst = []
        

    def addNum(self, num) :
        bisect.insort(self.lst, num)

    def findMedian(self) :
        mid = len(self.lst) // 2
        if  len(self.lst) % 2 == 0:
            return (self.lst[mid-1] + self.lst[mid]) / 2.0
        else:
            #print ((len(self.lst)-1) // 2)
            return self.lst[(len(self.lst)-1) // 2]
           
    #if else 可以合并
    # return (self.lst[len(self.lst) // 2] + self.lst[~(len(self.lst) // 2)]) / 2.0
        
if __name__ == "__main__":
    s = MedianFinder()
    s.addNum(1)
    s.addNum(2)
    #s.addNum(3)
    res = s.findMedian()
    print(res)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()