# 排序，每次加入一个最小值；
# 将remain = target-sum(tmp)作为参数进行递归，避免每次计算解中元素的和；
# 若remain < 0，则表示解中元素的和比target大，从解中pop最后一个元素；
# 若remain == 0，则找到一个解；
class Solution:
    def combinationSum(self, candidates, target):
        res = [] 
        candidates.sort()
        self.backtrace(res, [],candidates, target,0)
        return res
     #res 最后的结果，temp 传入可能加入res的值
    def backtrace(self, res, temp, candidates,remain, start):
        if remain < 0:
            return #不符合退出，继续找下一个
        if remain == 0:
            res.append(temp)
            return 
        for i in range(start, len(candidates)):
            self.backtrace(res, temp + [candidates[i]], candidates, remain - candidates[i], i) #可以重复使用同一元素，所以start是i而不是i+1


if __name__ == "__main__":
    s = Solution()
    res = s.combinationSum([2,3,5],8)
    print(res)