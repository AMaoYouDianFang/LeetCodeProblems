import collections
class Solution:
    def containsNearbyDuplicate(self, nums,k):
        d = collections.defaultdict(list)
        for i, nums in enumerate(nums):
            d[nums].append(i)
        for value in d.values():
            for i in range(len(value)):
                for j in range(i + 1, len(value)):
                    if abs(value[i]- value[j]) <= k:
                        return True
        return False

# 没有考虑[1],1
if __name__ == "__main__":
    s = Solution()
    res = s.containsNearbyDuplicate([1,2,3,1,2,3],2)
    print(res)
