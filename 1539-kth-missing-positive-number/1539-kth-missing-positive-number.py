class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lst=[]
        n=len(arr)-1
        
        for i in range(1,n+k+2):
            if i not in arr:
                lst.append(i)
        if lst[k-1]:
            return lst[k-1]
