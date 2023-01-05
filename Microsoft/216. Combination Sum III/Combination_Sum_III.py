class Solution:

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        output=[]

        

        def dfs(build,num,sum_so_far):

            if len(build)==k:

                if sum_so_far==n:

                    output.append(build)

                return

            for i in range(num,9+1):

                if sum_so_far+i>n:break

                dfs(build+[i],i+1,sum_so_far+i)

        dfs([],1,0)

        return output
