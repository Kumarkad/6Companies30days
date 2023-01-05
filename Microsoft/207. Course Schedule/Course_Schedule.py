class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        hashmap={i:[] for i in range(numCourses)}

        for crs,prs in prerequisites:

            hashmap[crs].append(prs)

        

        visitedSet=set()

        def dfs(crs):

            if crs in visitedSet:

                return False

            if hashmap[crs]==[]:

                return True

            visitedSet.add(crs)

            for prs in hashmap[crs]:

                if not dfs(prs):return False

            visitedSet.remove(crs)

            hashmap[crs]=[]

            return True

        for crs in range(numCourses):

            if not dfs(crs): return False

        return True

            
