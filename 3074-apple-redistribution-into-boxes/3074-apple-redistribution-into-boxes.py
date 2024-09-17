class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity=sorted(capacity,reverse=True)
        app_sum=sum(apple)
        c=0
        
        for num in capacity:
            if app_sum>0:
                app_sum-=num
                c+=1
        return c
        