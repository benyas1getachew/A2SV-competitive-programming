class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []

        for interval in intervals:
            start, end = interval
            events.append((start, 1))    
            events.append((end + 1, -1)) 
        events.sort()

        active_intervals = 0
        max_active = 0

        for time, event in events:
            active_intervals += event
            max_active = max(max_active, active_intervals)

        return max_active