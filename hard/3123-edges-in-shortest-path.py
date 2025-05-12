class Solution:
    def findAnswer(self, n: int, edges: list[list[int]]) -> list[bool]: 
        # if there are no nodes or edges, return empty list
        if n == 0 or not edges:
            return []
        
        # ---------------------------
        # 1. build the graph
        # ---------------------------
        # create adjacency list where graph[u] and graph[v] contains (neighbor, weight), since its an undirected graph (!DAG)
        #      node 0           node 1
        # [[(neighbor, weigh)], [(neighbor, weight)]]
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))  
            
        # ---------------------------
        # 2. dijkstra from start node (0)
        # ---------------------------
        def dijkstra(start: int) -> list[int]:
            distances = [float('inf')] * n
            distances[start] = 0            # weight 0 to reach starting node
            dijkstra_heap = [(0, start)]    
            visited = [False] * n
            
            while dijkstra_heap:
                dist, node = heapq.heappop(dijkstra_heap) # pops and corrects the heap automatically
                if visited[node]:
                    continue
                visited[node] = True
                
                # update distances for neighbors
                for neighbor, weight in graph[node]:
                    new_dist = dist + weight        # updating distance considering the last dist popped in line 41
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist  # verifying if the new_dist read is less than the actual distance
                        heapq.heappush(dijkstra_heap, (new_dist, neighbor))
            
            return distances
        
        # get shortest paths from start node (0)
        start_distances = dijkstra(0)
        
        # exit if there's no path to end node
        if start_distances[n-1] == float('inf'):
            return [False] * len(edges)
        
        # ---------------------------
        # 3. dijkstra from end node (n-1)
        # ---------------------------
        end_distances = dijkstra(n-1)
        
        # ---------------------------
        # 4. check each edge
        # ---------------------------
        shortest_path_length = start_distances[n-1] # that's the value to reach the 'n-1' node
        answer = []
        
        for u, v, w in edges:
            # check both directions since graph is undirected
            forward = start_distances[u] + w + end_distances[v]
            backward = start_distances[v] + w + end_distances[u]
            
            # edge is part of shortest path if either direction matches
            answer.append(forward == shortest_path_length or backward == shortest_path_length) # returns true if the edge is part of the shortest path
        
        return answer