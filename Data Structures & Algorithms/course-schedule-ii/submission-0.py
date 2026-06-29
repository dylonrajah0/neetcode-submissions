class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preMap = {i: [] for i in range(numCourses)}
        order = []
        for course, pre in prerequisites:
            preMap[course].append(pre)

        visiting = set()

        def dfs(course):

            if course in visiting:
                return False

            if preMap[course] == []:
                if course not in order:
                    order.append(course)
                return True
                
            visiting.add(course)

            for pre in preMap[course]:
                if not dfs(pre):
                    return False

            visiting.remove(course)
            preMap[course] = []
            order.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return order
            


        