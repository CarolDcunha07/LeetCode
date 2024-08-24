class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l=0
        left_sum=sum(nums)
        total=0
        
        for r in range(len(nums)):
            total+=nums[r]
            if total==left_sum:
                return r
            left_sum-=nums[l]
            l+=1
        return -1
        