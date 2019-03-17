from collections import defaultdict
class Solution():
    def killProcess(self, pid, ppid, kill):
        res = []
        stack = [kill]
        dic = defaultdict(list)
        for i in range(len(pid)):
            dic[ppid[i]].append(pid[i])
        while stack:
            temp = stack[-1]
            stack.pop()
            res.append(temp)
            for i in dic[temp]:
                stack.append(i)
        return res
        
    
if __name__ == "__main__":
    ppid = [3, 0, 5, 3]
    pid = [1, 3, 10, 5]
    s = Solution()
    res = s.killProcess(pid,ppid,5)
    print(res)



