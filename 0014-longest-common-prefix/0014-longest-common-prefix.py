class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        
        
        for word in strs[1:]:
            j=0
            i=0
            while i<len(prefix) and j<len(word) and prefix[i]==word[j]:
                j+=1
                i+=1
            prefix=prefix[:j]
        return prefix
        
            
        