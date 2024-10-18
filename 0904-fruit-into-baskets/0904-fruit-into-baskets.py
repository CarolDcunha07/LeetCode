class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        c=collections.defaultdict(int)
        l,total,res=0,0,0
        for r in range(len(fruits)):
            c[fruits[r]]+=1
            total+=1
            while len(c)>2:
                f=fruits[l]
                c[f]-=1
                total-=1
                l+=1
                if not c[f]:
                    c.pop(f)
            res=max(res,total)
        return res
            
            
            