class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n=len(piles)
        piles=piles[n//3:]
        k=0
        for i in range(0,len(piles),2):
            k+=piles[i]
        return k