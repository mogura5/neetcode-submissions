class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []

        for courses, pre in prerequisites:
            preMap[courses].append(pre)
        
        visitSet = set()
        def dfs(course):
            if course in visitSet:
                return False
            if preMap[course] == []:
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
        
