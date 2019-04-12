class Solution:
    def hIndex(self, citations):
        l = len(citations)
        citations = sorted(citations, reverse = True)
        for h in range(0, len(citations)):
            if h >= citations[h]:
                return h
        return len(citations) # citations 为一个元素或者个元素      
             
if __name__ == "__main__":
    s =Solution()
    res = s.hIndex([1]) 
    print(res)