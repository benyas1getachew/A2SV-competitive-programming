class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for ai, bi in prerequisites:
            graph[bi].append(ai)
            in_degree[ai] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        result = []
        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return result if len(result) == numCourses else []