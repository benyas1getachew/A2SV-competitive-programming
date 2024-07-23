class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        indexed_tasks = [(tasks[i][0], tasks[i][1], i) for i in range(n)]
        indexed_tasks.sort()

        min_heap = []
        time = 0
        index = 0
        result = []

        while index < n or min_heap:
            while index < n and indexed_tasks[index][0] <= time:
                heapq.heappush(min_heap, (indexed_tasks[index][1], indexed_tasks[index][2]))
                index += 1

            if min_heap:
                processing_time, task_index = heapq.heappop(min_heap)
                time += processing_time
                result.append(task_index)
            else:
                time = indexed_tasks[index][0]

        return result