class Solution:

    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        graph = collections.defaultdict(list) 

        for u, v, t in roads: 

            graph[u].append((v, t)) 

            graph[v].append((u, t)) 

        #2. times, ways array initializer 

        times = [float('inf')] * n 

        ways = [0] * n

        

        times[0] = 0 

        ways[0] = 1

        

        #3. dijkstra

        pq = [(0, 0)] # time, node 

        while pq: 

            old_t, u = heapq.heappop(pq) # current time, current node

            for v, t in graph[u]:

                new_t = old_t + t 

                

                # casual logic: update shorter path 

                if new_t < times[v]: 

                    times[v] = new_t 

                    ways[v] = ways[u] 

                    heapq.heappush(pq, (new_t, v)) 

                # if find same time path... update ways only 

                elif new_t == times[v]:

                    ways[v] += ways[u]

                    

        modulo = 10 ** 9 + 7 

        

        return ways[n-1] % modulo
