class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum=nums[0]
        maxsum=nums[0]
        l=0
        
        if len(nums)==1:
            return nums[0]
        
        for i in range(1,len(nums)):
            while cursum<0:
                cursum-=nums[l]
                l+=1
            cursum+=nums[i]
            maxsum=max(maxsum,cursum)
        return maxsum
        
        
        