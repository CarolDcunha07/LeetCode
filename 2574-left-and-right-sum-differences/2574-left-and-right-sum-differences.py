class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left=[0]*len(nums)
        right=[0]*len(nums)
        
        for i in range(1,len(nums)):
            left[i]=nums[i-1]+left[i-1]
            
        for i in range(len(nums)-2,-1,-1):
            right[i]=right[i+1]+nums[i+1]
            
        for i in range(len(left)):
            nums[i]=abs(left[i]-right[i])
        return nums
            
        