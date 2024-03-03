class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.extend(processorTime)
        processorTime.extend(processorTime)
        processorTime.sort()
        tasks.sort(reverse=True)
        k=0
        for i in tasks:
            processorTime[k]+=i
            k+=1
        mx=max(processorTime)
        return mx