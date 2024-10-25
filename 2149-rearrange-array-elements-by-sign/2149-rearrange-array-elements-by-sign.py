class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=[]
        n=[]
        
        for num in nums:
            if num<0:
                n.append(num)
            else:
                p.append(num)
        j=0
        k=0
        for i in range(len(nums)):
            if i%2==0:
                nums[i]=p[j]
                j+=1
            else:
                nums[i]=n[k]
                k+=1
        if j<len(p):
            nums+=p
        if k<len(n):
            nums+=q
        return nums
        