class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=''
        for word in s:
            if word.isalnum():
                new+=word
        news=new.lower()
        print(news)
        if news==news[::-1]:
            return True
        else:
            return False
        