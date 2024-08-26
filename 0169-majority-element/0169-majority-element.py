class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lst=list(set(nums))
        n=len(nums)
        
        for num in lst:
            if nums.count(num)>n//2:
                return num
        