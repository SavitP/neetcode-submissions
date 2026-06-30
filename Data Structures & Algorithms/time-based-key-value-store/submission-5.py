class TimeMap:

    def __init__(self):
        self.map = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        times = self.map[key]
        if times[0][0] > timestamp:
            return ""
        l = 0
        r = len(times)
        while l + 1 != r:
            mid = l + (r - l) // 2
            print(mid)
            if times[mid][0] == timestamp:
                return times[mid][1]
            if times[mid][0] < timestamp:
                l = mid
            else:
                r = mid
        return times[l][1]
