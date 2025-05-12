class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        print("=== BUILDING GRAPH ===")
        # Build adjacency list with both directions for undirected graph
        graph = defaultdict(list)
        for u, v, w in roads:
            print(f"Adding road between {u} <-> {v} with weight {w}")
            graph[u].append((w, v))
            graph[v].append((w, u))
        
        MOD = 10**9 + 7
        print(f"\n=== DATA STRUCTURES ===")
        print(f"Graph is {graph}")
        print("Initial min-heap with (cost 0, node 0)")
        min_heap = [(0, 0)]  # (cost, node)
        
        # Initialize shortest distances with infinity
        min_cost = [float('inf')] * n
        min_cost[0] = 0
        print(f"Initial min_cost array: {min_cost}")
        
        # Initialize path counts with 0s except starting node
        path_count = [0] * n
        path_count[0] = 1
        print(f"Initial path_count array: {path_count}\n")
        
        print("=== PROCESSING NODES WITH DJIKSTRA ===")
        while min_heap:
            current_cost, current_node = heapq.heappop(min_heap)
            print(f"\n> Processing node {current_node} with accumulated cost {current_cost}")
            
            # Skip if we found a better path already
            if current_cost > min_cost[current_node]:
                print(f"  Better path to {current_node} already exists ({min_cost[current_node]} < {current_cost}), skipping")
                continue
                
            print(f" Current best path count to {current_node}: {path_count[current_node]}")
            
            for weight, neighbor in graph[current_node]:
                new_cost = current_cost + weight
                print(f"\n  Evaluating neighbor {neighbor} (weight {weight})")
                print(f"  New cost: {new_cost} vs current: {min_cost[neighbor]}")
                
                if new_cost < min_cost[neighbor]:
                    print("  NEW shortest path found! Updating:")
                    min_cost[neighbor] = new_cost
                    path_count[neighbor] = path_count[current_node]
                    heapq.heappush(min_heap, (new_cost, neighbor))
                    print(f"    Updated min_cost[{neighbor}] = {new_cost}")
                    print(f"    Set path_count[{neighbor}] = {path_count[current_node]}")
                    print(f"    Pushed ({new_cost}, {neighbor}) to heap")
                    print(f"  Current heap state: {min_heap}")
                    print(f"  Current min_cost state: {min_cost}")
                elif new_cost == min_cost[neighbor]:
                    print("  EQUAL COST path found! Adding path counts:")
                    print(f"    Current path_count[{neighbor}]: {path_count[neighbor]}")
                    print(f"    Adding path_count[{current_node}]: {path_count[current_node]}")
                    path_count[neighbor] = (path_count[neighbor] + path_count[current_node]) % MOD
                    print(f"    Updated path_count[{neighbor}]: {path_count[neighbor]}")
                    print(f"  Current heap state: {min_heap}")
                    print(f"  Current min_cost state: {min_cost}")
                    
        print("\n=== RESULTS ===")
        print(f"Shortest distance to {n-1}: {min_cost[n-1]}")
        print(f"Number of shortest paths: {path_count[n-1]}")
        print(f"Path Count: {path_count}")
        
        return path_count[n-1] % MOD