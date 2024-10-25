class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        
        mprice=float('inf')
        
        for price in prices:
            mprice=min(price,mprice)
            p=max(p,price-mprice)
        return p
        