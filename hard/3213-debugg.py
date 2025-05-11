import heapq

class Solution:
    def findAnswer(self, n: int, edges: list[list[int]]) -> list[bool]:
        print(f"\n=== INITIALIZING PROBLEM ===")
        print(f"Nodes: {n}, Edges: {edges}")

        # Edge case handling
        if n == 0 or not edges:
            print("! Edge case: Empty input")
            return []
        
        # ---------------------------
        # 1. Build the graph
        # ---------------------------
        print("\n=== BUILDING GRAPH ===")
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
            print(f"Added edge: {u} <-> {v} (weight {w})")

        # ---------------------------
        # 2. Dijkstra from start node (0)
        # ---------------------------
        def dijkstra(start: int, name: str) -> list[int]:
            print(f"\n=== RUNNING DIJKSTRA FROM {name} ({start}) ===")
            distances = [float('inf')] * n
            distances[start] = 0
            heap = [(0, start)]
            visited = [False] * n
            
            print(f"Initial distances: {distances}")
            
            while heap:
                dist, node = heapq.heappop(heap)
                if visited[node]:
                    print(f"  Skipping already processed node {node}")
                    continue
                    
                visited[node] = True
                print(f"\nProcessing node {node} (current distance: {dist})")
                
                for neighbor, weight in graph[node]:
                    old_dist = distances[neighbor]
                    new_dist = dist + weight
                    
                    print(f"  Checking neighbor {neighbor} (weight {weight})")
                    print(f"  Current best distance to {neighbor}: {old_dist}")
                    print(f"  Potential new distance: {new_dist}")

                    if new_dist < old_dist:
                        distances[neighbor] = new_dist
                        heapq.heappush(heap, (new_dist, neighbor))
                        print(f"  !! Updated distance to node {neighbor} from {old_dist} to {new_dist}")
                        print(f"  Pushed ({new_dist}, {neighbor}) to heap")
                        print(f"  Current heap state: {heap}")
                    else:
                        print(f"  No improvement for {neighbor} (keep {old_dist})")
            print("\n                     Nodes: 0  1  2  3  4  5")
            print(f"Final distances from {name}: {distances}")
            return distances

        start_distances = dijkstra(0, "START")
        if start_distances[n-1] == float('inf'):
            print("\n!!! NO PATH EXISTS FROM START TO END !!!")
            return [False] * len(edges)

        # ---------------------------
        # 3. Dijkstra from end node (n-1)
        # ---------------------------
        end_distances = dijkstra(n-1, "END")

        # ---------------------------
        # 4. Check each edge
        # ---------------------------
        print("\n=== CHECKING EDGES ===")
        shortest_path_length = start_distances[n-1]
        print(f"Shortest path length: {shortest_path_length}")
        answer = []

        for i, (u, v, w) in enumerate(edges):
            forward = start_distances[u] + w + end_distances[v]
            backward = start_distances[v] + w + end_distances[u]
            
            print(f"\nEdge {i}: {u}-{v} (weight {w})")
            print(f"Forward path: {start_distances[u]} + {w} + {end_distances[v]} = {forward}")
            print(f"Backward path: {start_distances[v]} + {w} + {end_distances[u]} = {backward}")
            
            is_valid = forward == shortest_path_length or backward == shortest_path_length
            print(f"Valid? {'YES' if is_valid else 'NO'}")
            answer.append(is_valid)

        print("\n=== FINAL RESULT ===")
        print(answer)
        return answer