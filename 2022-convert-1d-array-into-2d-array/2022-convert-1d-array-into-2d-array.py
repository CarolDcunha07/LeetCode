class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans=[]
        temp=[]
        c=0
        
        if len(original)!=m*n:
            return []
        
        
        
        for val in original:
            temp.append(val)
            c+=1
            
            if c==n:
                ans.append(temp)
                temp=[]
                c=0
        return ans
        
                    
                    
            
                
        