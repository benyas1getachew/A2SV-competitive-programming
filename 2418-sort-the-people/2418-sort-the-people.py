class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dicts={}
        for i in range(len(heights)):
            dicts[heights[i]]=[i,0]
        heights.sort(reverse = True)
        
        for i in range(len(heights)):
            dicts[heights[i]][1]=i
        
        n_dict={}
        for i in dicts:
            n_dict[dicts[i][1]]=dicts[i][0]
        arr=names.copy()
        for i in range(len(arr)):
            arr[i]=names[n_dict[i]]
        return arr
            