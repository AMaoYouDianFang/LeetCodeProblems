class Solution:
    def findMinHeightTrees(self, n: int, edges):
        if n == 1: return [0]
        leaves = []
        adj = [set() for i in range(n)] 
        for edge in edges:
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])
        
        for i in range(n):
            if len(adj[i]) ==1:
                leaves.append(i)  #找出来叶子节点
        
        while n> 2:
            n = n - len(leaves)
            newleaves = []
            for i in leaves:
                t = adj[i].pop()
                adj[t].remove(i)
                if len(adj[t])==1:
                    newleaves.append(t)
            leaves = newleaves
        return leaves

if __name__ == "__main__":
    s= Solution()
    res = s.findMinHeightTrees(4,[[1, 0], [1, 2], [1, 3]])
    print(res)
        