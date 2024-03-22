class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {char: i for i, char in enumerate(s)}
        start = end = 0
        partitions = []

        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])
            if i == end:
                partitions.append(end - start + 1)
                start = i + 1

        return partitions
