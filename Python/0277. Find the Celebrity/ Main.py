class Solution(object):
    def findCelebrity(self, n): 
        if n == 0:
            return -1
        candidate = 0 
        for i in range(n):
            if knows(candidate, i):
                candidate = i #假设的candidate不是， i可能是
        for i in range(n):
            if i == candidate:
                continue
            if  not knows(i, candidate or knows(i, candidate):
                return -1
        
        return candidate

#https://www.youtube.com/watch?v=QDehNYXlCAg