class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)

        for u, v in redEdges:
            red_graph[u].append(v)
        for u, v in blueEdges:
            blue_graph[u].append(v)

        queue = deque([(0, 0, 'red'), (0, 0, 'blue')])
        visited = set([(0, 'red'), (0, 'blue')])
        answer = [-1] * n
        answer[0] = 0

        # BFS traversal
        while queue:
            node, length, last_color = queue.popleft()

            if last_color == 'red':
                next_edges = blue_graph[node]
                next_color = 'blue'
            else:
                next_edges = red_graph[node]
                next_color = 'red'

            for neighbor in next_edges:
                if (neighbor, next_color) not in visited:
                    visited.add((neighbor, next_color))
                    queue.append((neighbor, length + 1, next_color))
                    if answer[neighbor] == -1:
                        answer[neighbor] = length + 1

        return answer
