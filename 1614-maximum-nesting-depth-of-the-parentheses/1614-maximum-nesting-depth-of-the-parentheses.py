class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        ans=0
        
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(s[i])
            elif s[i]==')':
                if stack:
                    stack.pop()
            ans=max(ans,len(stack))
        return ans
        