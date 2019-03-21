class Solution:
    def findOrder(self, numCourses, prerequisites):
        res = []
        indegree = [0] * numCourses #表示每个点的入度
       
        graph = [ [] for i in range(numCourses)]
        for i in prerequisites:
            graph[i[1]].append(i[0])
            indegree[i[0]] += 1
        stack = []
        for i in range(numCourses):
            if indegree[i] == 0:
                stack.append(i)
        
        while stack:
            t = stack[0]
            res.append(t)
            stack.pop(0)
            for i in graph[t]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    stack.append(i)
        
        if len(res) != numCourses:
            res = []
       
        return res
