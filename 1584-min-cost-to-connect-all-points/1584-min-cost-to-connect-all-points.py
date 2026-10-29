import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)

        min_heap = [(0, 0)] 
        visited = set()
        total_cost = 0

        while len(visited) < n:
            cost, curr = heapq.heappop(min_heap)

            if curr in visited:
                continue

            visited.add(curr)
            total_cost += cost

            x1, y1 = points[curr]

            for nxt in range(n):
                if nxt not in visited:
                    x2, y2 = points[nxt]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(min_heap, (dist, nxt))

        return total_cost