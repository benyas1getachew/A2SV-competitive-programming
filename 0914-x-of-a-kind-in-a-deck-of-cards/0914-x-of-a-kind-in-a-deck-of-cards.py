class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)

        counts = list(count.values())

        overall_gcd = reduce(gcd, counts)

        return overall_gcd > 1