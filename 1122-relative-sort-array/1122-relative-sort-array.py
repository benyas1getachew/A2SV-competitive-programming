class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {val: idx for idx, val in enumerate(arr2)}

        def sort_key(x):
            return (order.get(x, 1001), x)

        return sorted(arr1, key=sort_key)
