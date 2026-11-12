class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = {}
        for t in tasks:
            if t not in m:
                m[t] = 0
            m[t] += 1
        largest = max(m.values())
        numLargest = 0
        for num in m.values():
            if num == largest:
                numLargest += 1
        return max(len(tasks), (largest - 1) * (n + 1) + numLargest)