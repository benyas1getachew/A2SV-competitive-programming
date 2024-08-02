class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        all_keys = 0
        start = None

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = (i, j)
                elif grid[i][j].islower():
                    all_keys |= (1 << (ord(grid[i][j]) - ord('a')))

        queue = deque([(start[0], start[1], 0, 0)])  
        visited = set()
        visited.add((start[0], start[1], 0))

        while queue:
            r, c, keys_collected, steps = queue.popleft()

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    char = grid[nr][nc]

                    if char == '#':
                        continue

                    new_keys = keys_collected
                    if char.islower():
                        new_keys |= (1 << (ord(char) - ord('a')))

                    if char.isupper() and not (new_keys & (1 << (ord(char.lower()) - ord('a')))):
                        continue

                    if new_keys == all_keys:
                        return steps + 1

                    if (nr, nc, new_keys) not in visited:
                        visited.add((nr, nc, new_keys))
                        queue.append((nr, nc, new_keys, steps + 1))

        return -1