class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {}
        result = []

        for course in range(numCourses):
            preMap[course] = []
        for course, pre in prerequisites:
            preMap[course].append(pre)

        visitedSet = set()
        cycle = set()
        
        def dfs(course):
            if course in cycle: #detected cycle
                return False
            if course in visitedSet: # we don't need to visit course twice 
                return True
            cycle.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visitedSet.add(course)
            result.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return result
