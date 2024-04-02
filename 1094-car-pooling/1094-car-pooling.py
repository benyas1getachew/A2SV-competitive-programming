class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        locations = [0] * 1001

        for trip in trips:
            num_passengers, start, end = trip
            locations[start] += num_passengers
            locations[end] -= num_passengers

        passengers = 0
        for passengers_change in locations:
            passengers += passengers_change
            if passengers > capacity:
                return False

        return True