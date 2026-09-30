class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if k > len(times):
            return -1
        seen = {}
        graph = {}
        for edge in times:
            if edge[0] not in graph:
                graph[edge[0]] = []
            graph[edge[0]].append([edge[1], edge[2]])
        seen[k] = 0
        heap = []
        if k not in graph:
            return -1
        for edge in graph[k]:
            heapq.heappush(heap, (edge[1], edge[0]))
        while len(heap) > 0:
            curr = heapq.heappop(heap)
            if curr[1] not in seen:
                seen[curr[1]] = curr[0]
                if curr[1] in graph:
                    for next in graph[curr[1]]:
                        if next[0] not in seen:
                            heapq.heappush(heap, (curr[0] + next[1], next[0]))
        if len(seen) < n:
            return -1
        m = 0
        for node in seen:
            if seen[node] > m:
                m = seen[node]
        return m
        
            
