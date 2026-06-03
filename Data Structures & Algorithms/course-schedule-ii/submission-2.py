class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {}
        order = []
        for course in range(numCourses):
            preMap[course] = []
        for course, pre in prerequisites:
            preMap[course].append(pre)
        visited = set()
        cycle = set()

        def dfs(course):

            # base case
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visited.add(course)
            order.append(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return order