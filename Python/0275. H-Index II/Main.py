class Solution:
    def hIndex(self, citations):
        l, r = 0,len(citations)-1
        lng = len(citations)
        
        while l <= r:
            mid = (l + r) // 2
            if citations[mid] == lng-mid:
                return lng-mid
            elif citations[mid] < lng-mid:
                l = mid + 1
            else:
                r = mid -1
        return lng - l

if __name__ == "__main__":
    s = Solution()
    res = s.hIndex([0,0])
    print(res)

        