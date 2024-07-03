class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i+1:]

        deadends = set(deadends)
        visited = set('0000')

        if '0000' in deadends:
            return -1

        queue = deque([('0000', 0)])  
        while queue:
            node, depth = queue.popleft()
            if node == target:
                return depth
            for neighbor in neighbors(node):
                if neighbor not in visited and neighbor not in deadends:
                    visited.add(neighbor)
                    queue.append((neighbor, depth + 1))

        return -1
