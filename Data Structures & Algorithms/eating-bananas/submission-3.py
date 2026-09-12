class Solution:
    def checkRate(self, num: int, piles: List[int], h: int) -> bool:
        total_hours=0
        for i in piles:
            if num==0:
                return True
            total_hours+=-(-i // num)
        if total_hours<=h:
            return True
        return False
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        while l<=r:
            mid=(l+r)//2
            if self.checkRate(mid,piles,h) and not self.checkRate(mid-1,piles,h):
                return mid
            elif self.checkRate(mid,piles,h):
                r=mid-1
            else:
                l=mid+1
        return 1