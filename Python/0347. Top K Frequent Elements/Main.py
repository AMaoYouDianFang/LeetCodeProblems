import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        res = []
        maps = collections.Counter(nums)
        print(maps)
        buskets = ['*'] * (len(nums) +1 ) #用* 是为了防止k>所有元素的种类
        # Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，
        # 以字典的键值对形式存储，其中元素作为key，其计数作为value。
        for key in maps.keys():
            count = maps[key]
            if buskets[count] == '*':
                buskets[count] = []
            buskets[count].append(key)

        i = len(nums)

        while len(res)< k and i>0:
            if buskets[i] != '*':
                res.extend(buskets[i]) 
            i -=1
            print(i)
        return res

if __name__ == "__main__":
    s = Solution()
    res = s.topKFrequent([1,1,1,2,2,3],2)
    print(res)


