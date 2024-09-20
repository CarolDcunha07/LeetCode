class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr)%3!=0:
            return False
        
        res=sum(arr)//3
        t=0
        c=0
        
        for i in range(len(arr)):
            t+=arr[i]
            if t==res:
                c+=1
                t=0
            if c==3:
                return True
        return c==3
        
        