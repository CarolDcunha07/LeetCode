class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)>len(goal):
            return False
        dup=s+s
        
        if goal in dup:
            return True
        else:
            return False
        