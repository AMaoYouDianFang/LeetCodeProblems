class Solution:
    def fourSum(self, nums, target):
        l = len(nums)
        nums = sorted(nums)
       
        res = []
        for a in range(l-3):
            for b in range(a+1, l-2):
                c = b + 1
                d = l - 1
                while c < d:
                    sum = nums[a] +nums[b] +nums[c] +nums[d]
                    if sum == target:
                        li = [nums[a] , nums[b] , nums[c] , nums[d]]
                        if li not in res:
                            res.append(li)
                        c += 1
                        d -= 1
                    elif sum > target:
                        d -= 1
                    else:
                        c += 1
        return res

            

if __name__ == "__main__":
    solution = Solution()
    res = solution.fourSum([1,0,-1,0,-2,2],0)
    print(res)