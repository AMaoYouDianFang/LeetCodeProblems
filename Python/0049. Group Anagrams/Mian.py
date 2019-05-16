from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in range(len(strs)):
            lst = list(strs[i])
            res = "".join(sorted(lst))
            d[res].append(strs[i]) # d[res] = d[res].append(strs[i]) is error
        ls = []
        for key in d.keys():
            ls.append(d[key])
        return ls


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))