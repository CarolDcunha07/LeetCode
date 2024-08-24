class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lst=[]
        
        for num in nums:
            if num not in lst:
                lst.append(num)
        
        for i in range(len(lst)):
            nums[i]=lst[i]
        return len(lst)
        