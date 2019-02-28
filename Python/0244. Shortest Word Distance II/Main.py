#这道题是上题的follow up， 假如要多次调用应该如何优化。 我们可以维护
# 一个dic里面存储每个word 以及出现的坐标index。这样查询的时候我们
# 只需要get这两个单词的list，然后进行比较就可以了, 因为两个list都是排序后的， 
# 所以我们可以用类似merge two sorted list的方法来计算minDistance
import collections,sys
class WordDistance:
    def __init__(self, words):
        self.lookup = collections.defaultdict(list)
        for i , w in enumerate(words):
            self.lookup[w].append(i)

    def shortest(self, word1, word2):
        lst1 = self.lookup[word1]
        lst2 = self.lookup[word2]
        res = sys.maxsize
        # for i in lst1:
        #     for j in lst2:
        #         res = min(res, abs(i-j))
        ####two sort merge 方法
        i = 0
        j = 0
        while i < len(lst1) and j <len(lst2):
            res = min(res, abs(lst1[i] - lst2[j]))
            if lst1[i] < lst2[j]:
                i += 1
            else:
                j += 1
        return res

if __name__ == "__main__":
    s = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
    res = s.shortest('coding', 'practice')
    print(res)