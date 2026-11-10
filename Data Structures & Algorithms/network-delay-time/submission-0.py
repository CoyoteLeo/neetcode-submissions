class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(dict)
        for s, d, t in times:
            adj[s][d] = t

        heap = [(0, k)]
        dist = {}
        while heap:
            t, node = heapq.heappop(heap)

            if node in dist:
                continue
            
            dist[node] = t

            for neighbor, weight in adj[node].items():
                if neighbor not in dist:
                    heapq.heappush(heap, (t + weight, neighbor))

        return max(dist.values()) if len(dist) == n else -1