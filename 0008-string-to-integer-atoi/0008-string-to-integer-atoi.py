import sys
class Solution:
    def myAtoi(self, s: str) -> int:
        res=''
        s=s.strip()
        
        res1=''
        res2=''
        
        if len(s)==0:
            return 0
        
        if s[0]=='+' or s[0]=='-' or s[0].isdigit():
            res1+=s[0]
        if s[0].isalpha() or s[0]=='.':
            return 0
            
        for i in range(1,len(s)):
            if s[i].isdigit() and (s[i-1]!='.' or s[i-1].isalpha() or s[i-1].isspace()):
                res2+=s[i]
            if s[i]=='-' or s[i]=='+' or s[i].isalpha() or s[i].isspace() or s[i]=='.':
                break
            
        print(res1)
        print(res2)
        
        res=res1+res2
        
        if res=='':
            res=0
        elif res=='+' or res=='-':
            res=0
        else:
            res=int(res)
            
        if res>(2)**31-1:
            res=(2)**31-1
        if res<(-2)**31:
            res=(-2)**31
        return res
                
        