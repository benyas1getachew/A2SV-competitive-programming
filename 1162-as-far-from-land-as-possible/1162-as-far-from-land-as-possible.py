class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if not grid or not grid[0]:
            return -1

        queue = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))

        if len(queue) == 0 or len(queue) == n * n:
            return -1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        distance = -1
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                        grid[nx][ny] = 1  
                        queue.append((nx, ny))
            distance += 1

        return distance