class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        left=0
        
        for i in range(len(nums)):
            left+=nums[i]
            
            if left==total:
                return i
            total-=nums[i]
        return -1
        