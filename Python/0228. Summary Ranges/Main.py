#https://leetcode.com/problems/summary-ranges/discuss/185327/Java-one-pass-solution-beats-100-O(1)-extra-space-%2B-explanation
class Solution:
    def summaryRanges(self, nums):
        res = []
        length = 1
        for i in range(1, len(nums) + 1): #注意是+1，纠结了很久。。
            if i < len(nums) and nums[i] == nums[i-1] + 1:
                length += 1
            else: 
                if length == 1:
                    res.append(str(nums[i-1]))
                else:
                    res.append(str(nums[i-length]) + "->" +str(nums[i-1]))
                length = 1
        return res

if __name__ == "__main__":
    s = Solution()
    res = s.summaryRanges([0,1,2,4,5,7])
    print(res)