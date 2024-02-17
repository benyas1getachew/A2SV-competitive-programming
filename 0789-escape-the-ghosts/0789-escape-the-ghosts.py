class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        mi=0
        for k in ghosts:
            dis=abs(target[0]-k[0])+abs(target[1]-k[1])
            if dis<mi or mi==0:
                mi=dis
        
        dist=abs(target[0])+abs(target[1])
        
        if dist>=mi:
            return False
        else:
            return True