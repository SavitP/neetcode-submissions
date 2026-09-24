class Solution:
    def canFinish(self, numCourses: int, prereqs: List[List[int]]) -> bool:
        m = {}
        for l in prereqs:
            if l[0] not in m:
                m[l[0]] = set()
            m[l[0]].add(l[1])
        good = set()
        visited = set()
        print(m)
        def explore(course):
            print(course)
            if course in m:
                for next in m[course]:
                    if next in visited:
                        return False
                    if next not in good:
                        visited.add(next)
                        if explore(next) == False:
                            return False
            good.add(course)
            visited.remove(course)
            return True
        for course in m.keys():
            visited.add(course)
            if explore(course) == False:
                return False
        return True
        