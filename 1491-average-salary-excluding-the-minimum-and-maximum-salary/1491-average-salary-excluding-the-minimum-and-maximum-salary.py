class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        
        total=sum(salary)
        
        if len(salary)>=2:
            stotal=total-salary[0]-salary[len(salary)-1]
        
        avg=stotal/(len(salary)-2)
        return avg
            
        