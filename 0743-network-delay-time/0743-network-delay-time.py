import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, k)] 
        dist = {}

        while pq:
            time, node = heapq.heappop(pq)

            if node in dist:
                continue

            dist[node] = time

            for neighbor, weight in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(pq, (time + weight, neighbor))

        if len(dist) != n:
            return -1

        return max(dist.values())