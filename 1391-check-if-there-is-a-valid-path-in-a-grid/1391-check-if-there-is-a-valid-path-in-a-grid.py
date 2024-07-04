class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        directions = {
            1: [(0, -1, [1, 4, 6]), (0, 1, [1, 3, 5])],
            2: [(-1, 0, [2, 3, 4]), (1, 0, [2, 5, 6])],
            3: [(0, -1, [1, 4, 6]), (1, 0, [2, 5, 6])],
            4: [(0, 1, [1, 3, 5]), (1, 0, [2, 5, 6])],
            5: [(0, -1, [1, 4, 6]), (-1, 0, [2, 3, 4])],
            6: [(0, 1, [1, 3, 5]), (-1, 0, [2, 3, 4])]
        }

        def is_valid(x, y, nx, ny):
            if 0 <= nx < m and 0 <= ny < n:
                for d in directions[grid[x][y]]:
                    if d[0] == nx - x and d[1] == ny - y and grid[nx][ny] in d[2]:
                        return True
            return False

        queue = deque([(0, 0)])
        visited = set((0, 0))

        while queue:
            x, y = queue.popleft()
            if (x, y) == (m - 1, n - 1):
                return True
            for dx, dy, _ in directions[grid[x][y]]:
                nx, ny = x + dx, y + dy
                if is_valid(x, y, nx, ny) and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        return False