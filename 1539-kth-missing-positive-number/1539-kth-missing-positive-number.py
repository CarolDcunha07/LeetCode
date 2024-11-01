class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        c=k
        lst=[]
        for i in range(1,k+1+len(arr)):
            if i not in arr:
                lst.append(i)
                print(lst)
                if c>0:
                    c-=1
                else:
                    return lst[k-1]
        return lst[k-1]
                
            
        