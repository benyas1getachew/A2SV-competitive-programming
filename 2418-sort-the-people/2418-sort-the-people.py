class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dicts={}
        for i in range(len(heights)):
            dicts[heights[i]]=names[i]
        dicts=dict(sorted(dicts.items(),reverse = True))
        k=0
        for i in dicts:
            names[k]=(dicts[i])
            k+=1
        return names
            