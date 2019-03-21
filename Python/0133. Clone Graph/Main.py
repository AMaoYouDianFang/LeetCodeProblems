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
        if node in dic.keys():
            return dic[node]
        clone = Node(node.val,[])
        dic[node] = clone
        for neighbor in node.neighbors:
            clone.neighbors.append(self.helper(neighbor,dic))
        return clone
        
