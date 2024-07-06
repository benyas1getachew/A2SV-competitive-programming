class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source== target:
            return 0
        
        stop_to_routes = defaultdict(set)
        for route_id, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(route_id)

        queue = deque([(source, 0)])
        visited_stops = set([source])
        visited_routes = set()
        
        while queue:
            current_stop, buses_taken=queue.popleft()
            
            for route_id in stop_to_routes[current_stop]:
                if route_id in visited_routes:
                    continue
                visited_routes.add(route_id)

                for stop in routes[route_id]:
                    if stop == target:
                        return buses_taken + 1
                    if stop not in visited_stops:
                        visited_stops.add(stop)
                        queue.append((stop, buses_taken + 1))

        return -1