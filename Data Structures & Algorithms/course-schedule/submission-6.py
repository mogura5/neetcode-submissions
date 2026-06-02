class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {} 
        for i in range(numCourses):
            preMap[i] = []  # Hashmap: For every course, we have en empty list
        # for each prerequisite, we want to append to list
        for course, pre in prerequisites:
            preMap[course].append(pre)
        visitSet = set() # all sources along the curr DFS path
        def dfs(course):
            if course in visitSet: # base case: detected a loop 
                return False
            if preMap[course] == []: # base case: course has no prereq
                return True
            visitSet.add(course)
            for pre in preMap[course]: # Recrusively now call the course 
                if not dfs(pre):
                    return False
            visitSet.remove(course) # no longer visiting the class
            preMap[course] = [] # do not have to repeat dfs on all 
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True