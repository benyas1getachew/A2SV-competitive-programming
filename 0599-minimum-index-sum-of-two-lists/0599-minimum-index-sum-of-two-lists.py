class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common=set(list1)& set(list2)
        
        min_index=float('inf')
        result=[]
        for rest in common:
            index=list1.index(rest)+list2.index(rest)
            if index<min_index:
                min_index=index
                result=[rest]
            elif index== min_index:
                result.append(rest)
        return result