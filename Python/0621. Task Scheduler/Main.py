class Solution(object):
    def leastInterval(self, tasks, n):
        l = len(tasks)
        cnt = [ 0 ] * 26
        for tasks in tasks:
            cnt[ord(tasks) - ord('A')] += 1
        cnt.sort()
        i = 0
        mx = cnt[-1]
        
        while cnt[-1] == mx:
            cnt.pop()
            i += 1
        
        return max(l, (mx-1)*(n+1) + i )
       

if __name__ == "__main__":
    s = Solution()
    res = s.leastInterval(["A","A","A","B","B","B"],0)
    print(res)