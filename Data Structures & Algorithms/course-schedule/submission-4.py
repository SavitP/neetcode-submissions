class Solution:
    def canFinish(self, numCourses: int, prereqs: List[List[int]]) -> bool:
        m = {}
        self.visited = set()
        for course in prereqs:
            if course[0] not in m:
                m[course[0]] = []
            m[course[0]].append(course[1])
        def explore(num):
            if num not in m:
                return True
            while len(m[num]) > 0:
                n = m[num].pop()
                if n in self.visited:
                    return False
                self.visited.add(n)
                if not explore(n):
                    return False
                self.visited.remove(n)
            del m[num]
            return True

        for i in range(numCourses):
            if i in m:
                self.visited = {i}
                if not explore(i):
                    return False
        return True
