class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        #visit set to store all courses along the current DFS path
        visitSet = set()
        def dfs(course):

            # base cases
            if course in visitSet: # detected a loop
                return False
            if preMap[course] == []: # no prerequisites, so it can be completed
                return True

            visitSet.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False

            visitSet.remove(course)
            preMap[course] = []
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True