class Solution:
    def check(self, nums: List[int]) -> bool:
        i=0
        
        while i <len(nums):
            
            if sorted(nums[i:]+nums[:i])==(nums[i:]+nums[:i]):
                return True
            i+=1
        return False
                
                
        