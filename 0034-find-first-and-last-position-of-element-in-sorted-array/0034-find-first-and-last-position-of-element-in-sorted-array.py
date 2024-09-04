class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        c=nums.count(target)
        
        if target in nums:
            idx=nums.index(target)
        else:
            return [-1,-1]
        
        return [idx,c+idx-1]
        
        
        