from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums=[str(x) for x in nums]
        
        def compare(a,b):
            if a+b>b+a:
                return -1
            else:
                return 1
            
            
        str_nums.sort(key=cmp_to_key(compare))
        if str_nums[0]=='0':
            return '0'
        
        return ''.join(str_nums)