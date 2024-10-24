class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z=[]
        l=[]
        res=[]
        
        for num in nums:
            if num==0:
                z.append(num)
            else:
                l.append(num)
        res=l+z
        
        for i in range(len(nums)):
            nums[i]=res[i]
        return nums
        