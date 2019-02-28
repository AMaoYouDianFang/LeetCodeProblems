import collections,sys
class Solution():
    def shortestWordDistance(self, words, word1, word2):
        lookup = collections.defaultdict(list)
        for index, w in enumerate(words):
            lookup[w].append(index)
        res = sys.maxsize
        if word1 == word2:
            indexs = lookup[word1]
            
            for i in range(len(indexs)):
                for j in range(i+1, len(indexs)):
                    res = min(res, abs(indexs[i] - indexs[j]))
            return res

        indexs_1 = lookup[word1]
        indexs_2 = lookup[word2]
        for i in range(len(indexs_1)):
            for j in range(len(indexs_2)):
                res = min(res, abs(indexs_1[i] - indexs_2[j]))
        return res
    
if __name__ == "__main__":
    s = Solution()
    nums = ["practice", "makes", "perfect", "coding", "makes"]
    res = s.shortestWordDistance(nums, 'practice', 'makes')
    print(res)


        


