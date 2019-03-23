import collections
class Solution:
    def findItinerary(self, tickets):
        lookup = collections.defaultdict(list)
        for start, end in sorted(tickets):  #排序后倒叙
            lookup[start].append(end)
        route = []
        stack = ['JFK']
        while stack:
            t = stack[-1]
            #print(t)
            if lookup[t] == []:
                route.insert(0,t)
                stack.pop()
                #print(route)
            else:
                stack.append(lookup[t][0])
                lookup[t].pop(0)
        return route


if __name__ == "__main__":
    s = Solution()
    res = s.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])
    print(res)