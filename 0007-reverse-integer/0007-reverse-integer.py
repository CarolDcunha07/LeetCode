class Solution:
    def reverse(self, x: int) -> int:
        num=str(x)
        
        if num[0]=='-':
            res=num[1:]
            ans='-'+res[::-1]
        else:
            ans=num[::-1]
        ans=int(ans)
        
        if ans<(-2)**31 or ans>((2**31)-1):
            return 0
        return ans
        