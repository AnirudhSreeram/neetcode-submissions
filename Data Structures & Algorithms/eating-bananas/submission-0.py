from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def does_k_work(k):
            hours = 0
            for p in piles:
                hours += ceil(p/k)
            return hours <= h

        l = 1
        r = max(piles)

        while l < r:
            k = (l+r) // 2 
            if does_k_work(k):
                r = k
            else:
                l = k + 1
        return r
                
        
            
        



