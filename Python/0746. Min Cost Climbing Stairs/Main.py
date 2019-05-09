from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        d = [None] * l
        d[0] = cost[0]
        d[1] = cost[1]
        for i in range(2, l):
            d[i] = min(d[i-1], d[i-2]) + cost[i]
        return min(d[l-1],d[l-2])
        
    #T: O(n) S: O(1)
    def minCostClimbingStairs1(self, cost: List[int]) -> int:
        l = len(cost)
        d = [None] * l
        first = cost[0]
        second = cost[1]
        for i in range(2, l):
            cur = min(first, second) + cost[i]
            first = second
            second = cur
        return min(first,second)

if __name__ == "__main__":
    s= Solution()
    print(s.minCostClimbingStairs([1,2,4,2]))
    print(s.minCostClimbingStairs1([1,2,4,2]))