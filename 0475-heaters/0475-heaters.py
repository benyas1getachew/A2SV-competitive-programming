class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def canCoverAllHouses(radius):
            i = 0 
            for heater in heaters:
                while i < len(houses) and houses[i] <= heater + radius:
                    if houses[i] >= heater - radius:
                        i += 1
                    else:
                        break
            return i == len(houses)

        left, right = 0, max(max(houses) - min(heaters), max(heaters) - min(houses))

        while left < right:
            mid = (left + right) // 2
            if canCoverAllHouses(mid):
                right = mid
            else:
                left = mid + 1

        return left