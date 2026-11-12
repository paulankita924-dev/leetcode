class Solution:
    def areConnected(self, n: int, threshold: int, queries: list[list[int]]) -> list[bool]:
        parent = list(range(n + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for d in range(threshold + 1, n + 1):
            multiple = 2 * d
            while multiple <= n:
                union(d, multiple)
                multiple += d

        return [find(a) == find(b) for a, b in queries]