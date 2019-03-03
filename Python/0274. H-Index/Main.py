class Solution:
    def hIndex(self, citations):
        l = len(citations)
        citations = sorted(citations, reverse = True)
        for h in range(0, len(citations)):
            if h >= citations[h]:
                return h
        return len(citations)
        
            


if __name__ == "__main__":
    s =Solution()
    res = s.hIndex([4,4,4,4,4]) 
    print(res)