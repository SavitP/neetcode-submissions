class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        m = {i: [] for i in range(n)}
        for a, b in edges:
            m[a].append(b)
            m[b].append(a)
        visited = set()
        def explore(num, parent):
            if num in visited:
                return False
            visited.add(num)
            for nxt in m[num]:
                if nxt == parent:
                    continue
                if not explore(nxt, num):
                    return False
            return True
        return explore(0, -1) and len(visited) == n