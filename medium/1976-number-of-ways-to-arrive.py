class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # building adjacency list
        adj_list = defaultdict(list)
        # since it's undirected, map for both sides (u -> v, v -> u)
        for u, v, w in roads:
            adj_list[u].append((w, v))
            adj_list[v].append((w, u))
       
        mod = 10**9 + 7
        min_heap = [(0, 0)] # (cost, node) starting from node 0
        min_cost = [float('inf')] * n # making the value to any other nodes infinite
        path_count = [0] * n
        path_count[0] = 1

        while min_heap:
            cost, node = heappop(min_heap)

            for neighbor_cost, neighbor in adj_list[node]:
                if cost + neighbor_cost < min_cost[neighbor]:
                    min_cost[neighbor] = cost + neighbor_cost # found new min_cost
                    path_count[neighbor] = path_count[node]
                    heappush(min_heap, (cost + neighbor_cost, neighbor))
                elif cost + neighbor_cost == min_cost[neighbor]:
                    path_count[neighbor] = (path_count[neighbor] + path_count[node]) % mod
            
        return path_count[n-1]