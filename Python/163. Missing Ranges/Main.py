class Solution:
    def findMissingRanges(self, nums, lower, upper):
      
        length = 0
        res = []
        
        if lower < nums[0]:
            missing = str(lower) + '->' + str(nums[0]-1) if lower != nums[0]-1 else str(lower)
            res.append(missing)
        for i in range(1, len(nums)):
            if nums[i] < lower:
                continue
            elif nums[i] > upper:
                break
            else:
                if nums[i] != nums[i-1] + 1:
                    length = nums[i] - nums[i-1] -1
                    if length==1:
                        res.append(str(nums[i]-1))
                    else:
                        res.append(str(nums[i]-length)+ '->'+ str(nums[i]-1))
                else:
                    length =0
        if upper > nums[-1]:
            missing = str(nums[-1]+1) + '->' + str(upper) if upper != nums[-1]+1 else str(upper)
            res.append(missing)
        return res

if __name__ == "__main__":
    s = Solution()
    res = s.findMissingRanges([1, 3, 50, 75],-10,99)
    print(res)