class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.first = None
        self.cap = capacity
        self.size = 0
        self.last = None

    def get(self, key: int) -> int:
        if key in self.map:
            self.put(key, self.map[key][0])
            return self.map[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            if key == self.first:
                self.map[key][0] = value
                return
            if self.map[key][1] is not None:
                self.map[self.map[key][1]][2] = self.map[key][2]
            if self.map[key][2] is not None:
                self.map[self.map[key][2]][1] = self.map[key][1]
            if key == self.last is not None:
                self.last = self.map[key][1]
            self.map[key][1] = None
            self.map[key][2] = self.first
            self.map[self.first][1] = key
            self.map[key][0] = value
            self.first = key
        else:
            self.size += 1
            if self.size > self.cap:
                old = self.last
                prev = self.map[old][1]
                self.map.pop(old)
                self.last = prev
                if prev is not None:
                    self.map[prev][2] = None
                else:
                    self.first = None
                self.size -= 1
            self.map[key] = [value, None, self.first]
            if self.first is not None:
                self.map[self.first][1] = key
            if self.last is None:
                self.last = key
            self.first = key
        print(self.size)
        print(self.last)
            
