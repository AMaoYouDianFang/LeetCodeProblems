class Solution:

    def __init__(self, nums: List[int]):
        self.ori = nums
        self.res  = nums.copy()  #一定用copy

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.ori
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        import random
        for i in range(0,len(self.res)):
            j = random.randint(i,len(self.res)-1)
            self.res[i] ,self.res[j] = self.res[j], self.res[i]
        return self.res
        
        
    

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()