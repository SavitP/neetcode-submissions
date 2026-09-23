class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        r = k
        count = 0
        for i in range(k):
            if blocks[i] == "W":
                count += 1
        m = count
        while r < len(blocks):
            if blocks[r] == "W":
                count += 1
            if blocks[l] == "W":
                count -= 1
            m = min(m, count)
            l += 1
            r += 1
        return m

        