# Question 3
# Shortest Path Visiting all Nodes

# You have an undirected, connected graph of n nodes labeled from 0 to n - 1.
# You are given an array graph where graph[i] is a list of all nodes connected
# with node i by an edge.
# Return the length of the shortest path that visits every node. You may start and stop at any node,
# you may revisit nodes multiple times, and you may reuse edges.

from collections import deque

def shortestPathLength(graph):
    n = len(graph)
    final_mask = (1 << n) - 1
    queue = deque([[i, 1 << i, 0] for i in range(n)])
    visited = set((i , 1 << i) for i in range(n))
    while queue:
            node, mask, steps = queue.popleft()
            if mask == final_mask:
                return steps
            for neighbor in graph[node]:
                 new_mask = mask | (1 << neighbor)
                 if (neighbor, new_mask) not in visited:
                      visited.add((neighbor, new_mask))
                      queue.append([neighbor, new_mask, steps + 1])
if __name__ == '__main__':
     graph = [[1,2,3],[0],[0],[0]]
     print(shortestPathLength(graph))