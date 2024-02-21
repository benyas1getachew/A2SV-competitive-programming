class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        k=capacity
        cnt=0
        for i in range(len(plants)):
            if k>= plants[i]:
                cnt+=1
                k-=plants[i]
            else:
                cnt+=((i)*2)+1
                k=capacity-plants[i]
        return cnt