class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses

        for dest, src in prerequisites:
            adj_list[src].append(dest)
            in_degree[dest] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        processed_courses = 0

        while queue:
            course = queue.popleft()
            processed_courses += 1

            for neighbor in adj_list[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return processed_courses == numCourses