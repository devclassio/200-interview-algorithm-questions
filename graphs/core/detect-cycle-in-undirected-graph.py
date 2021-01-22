'''
Given an undirected graph, write a function to detect whether a cycle exists in a graph.

**Cycle definition**: A cycle is defined as a non empty path where the first and last vertix are identical.

**Cycle Example 1**: `A<->A`

**Cycle Example 2**: `A<->B<->A`

**Cycle Example 3**: `A<->B<->C<->A`
'''


class Solution:
    UNVISITED = 1
    VISITING = 2
    VISITED = 3
    FOUND_CYCLE = False

    def is_cyclic(self, graph):
        visit_state = {k: Solution.UNVISITED for k in graph}
        q = []
        for node, neighbors in graph.items():
            if len(neighbors) == 0:
                q.append(node)

        def dfs_with_cycle_check(q):
            if not q:
                return
            while q:
                current = q.pop(0)
                if visit_state[current] == Solution.VISITING:
                    return True
                visit_state[current] = Solution.VISITING
                for neighbor in graph[current]:
                    q.append(neighbor)
                    dfs_with_cycle_check(q)
                visit_state[current] = Solution.VISITED
            return False

        for vertex in graph:
            if (dfs_with_cycle_check(vertex)):
                return True
        return False
