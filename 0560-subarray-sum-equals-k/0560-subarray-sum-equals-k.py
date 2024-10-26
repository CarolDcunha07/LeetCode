class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c=0
        prefixsum=0
        prefixsum_count={0:1}
        
        for num in nums:
            prefixsum+=num
            if prefixsum-k in prefixsum_count:
                c+=prefixsum_count[prefixsum-k]
            if prefixsum in prefixsum_count:
                prefixsum_count[prefixsum]+=1
            else:
                prefixsum_count[prefixsum]=1
        return c
        