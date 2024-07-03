class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])  
        visited = set()
        visited.add((entrance[0], entrance[1]))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

        while queue:
            row, col, steps = queue.popleft()

            if (row != entrance[0] or col != entrance[1]) and (row == 0 or row == rows - 1 or col == 0 or col == cols - 1):
                return steps

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited and maze[new_row][new_col] == '.':
                    queue.append((new_row, new_col, steps + 1))
                    visited.add((new_row, new_col))

        return -1