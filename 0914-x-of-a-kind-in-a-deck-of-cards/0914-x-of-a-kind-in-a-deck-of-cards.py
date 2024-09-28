class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)

        # Get the counts of the card occurrences
        counts = list(count.values())

        # Calculate the GCD of all counts
        overall_gcd = reduce(gcd, counts)

        # Check if the GCD is greater than 1
        return overall_gcd > 1