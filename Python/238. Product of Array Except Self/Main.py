class Solution:
    def productExceptSelf(self, nums):
        l = len(nums)
        pref_prod = [nums[0]] * l #前缀乘积
        stuff_prod = [nums[-1]] * l

        for i in range (1,l):
            pref_prod[i] = pref_prod[i-1] * nums[i]

        for i in range (l -2, -1 ,-1): #是到0 ，不包括-1
            stuff_prod[i] = stuff_prod[i+1] * nums[i]
        
        res = [[0]] * l
        res[0] = stuff_prod[1]
        res[-1] = pref_prod[-2]

        for i in range(1, l-1):
            res[i] = pref_prod[i-1] * stuff_prod[i+1]
        return res
if __name__ == "__main__":
    s = Solution()
    res =s.productExceptSelf([1,2,3,4])
    print(res)