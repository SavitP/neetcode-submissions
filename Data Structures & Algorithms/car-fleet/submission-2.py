class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        map = {}
        for i in range(len(position)):
            map[position[i]] = speed[i]
        position.sort()
        counter = 0
        for i in range(len(position)):
            for j in range(i + 1, len(position)):
                if map[position[i]] > map[position[j]] and position[j] + (((position[j] - position[i]) / (map[position[i]] - map[position[j]])) * map[position[j]]) <= target:
                    counter += 1
                    break
        return len(position) - counter
