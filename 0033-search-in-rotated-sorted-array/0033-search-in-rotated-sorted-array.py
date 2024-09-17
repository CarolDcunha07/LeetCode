class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            idx=nums.index(target)
            return idx
        else:
            return -1
        