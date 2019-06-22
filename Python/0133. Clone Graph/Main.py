class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        dic = {}
        return self.helper(node, dic)
        
    def helper(self, node, dic):
        if not node: return None
        clone = Node(node.val,[])
        dic[node] = clone
        for n in node.neighbors:
            if n in dic.keys():
                clone.neighbors.append(dic[n])
            else:
                clone.neighbors.append(self.helper(n,dic))
        return clone
                
        
