class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        
        lst=s.split(" ")
        rev=lst[::-1]
        words=[]
        
        for word in rev:
            if word!='':
                words.append(word)
                
        res=' '.join(x for x in words)
        return res
        