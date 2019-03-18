# Definition for a binary tree node.
# graph 为 tree 两个条件：

# 这个图完全connected
# 没有cycle
    
class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        g = [[] for in range(n)]
        v = [False] * n
        for edge in edges:  #用二维数组寸图
            g[edge[0]].append(edge[1])
            g[edge[1]].append(edge[0])
        if self.dfs(g,v,0,-1) == False:  #表示连接中有环
            return False
        
        for i in v:  #遍历每个节点，有没有被访问的，图不是联通图
            if i ==False:
                return False
        return True
        
    def dfs(self, g, v, cur, pre):
        if v[cur] == True:  #v表示某一个节点是否被访问过
            return False
        v[cur] = True
        for i in g[cur]:
            if i != pre:  #i 不是当前节点的父节点，都收子节点
                if self.dfs(g,v,i, cur) == False:
                    return False
        return True

        

