class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        k=[]
        for i in range(len(fronts)):
            if fronts[i]==backs[i]:
                k.append(fronts[i])
        
        mi=0
        for i in range(len(fronts)):
            if not(fronts[i] in k):
                if fronts[i]<mi or mi==0:
                    mi=fronts[i]
            if not(backs[i] in k):
                if backs[i]<mi or mi==0:
                    mi=backs[i]
        
                
        return mi