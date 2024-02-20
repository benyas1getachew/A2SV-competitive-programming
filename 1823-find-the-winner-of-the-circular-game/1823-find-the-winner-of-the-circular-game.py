class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends_circle = list(range(1, n + 1)) 
        current_index = 0  
        while len(friends_circle) > 1:
             
            
            current_index += k-1  
            current_index %= len(friends_circle)  
            
            print(friends_circle.pop(current_index))

            if current_index == len(friends_circle):
                current_index = 0
        return friends_circle[0]