'''
Before we discuss implementations let's understand what a Topological sort. A topological sort is a linear ordering of vertices such that for every directed edge `uv` from vertex `u` to `v`, `u` comes before `v`.

- **We can only get a valid topological sort on a DAG (directed acyclic graph)**
- **By definition, cyclic graphs don't have valid topological sortings**.

So let's look at the following directed graph:

`t->u->v->w`
'''

graph = {
    '0': '1',
    '1': '2',
    '2': '3',
    '3': '4',
}

# Iterative Implementation


def iterative_top_sort(graph):
    indegrees = {vertex: 0 for vertix in graph}
    for vertex, neighbor in graph.items():
        indegrees[neighbor] += 1

    q, top_ordering = [], []
    for vertex in graph:
        if indegrees[vertex] == 0:
            q.append(vertex)

    while q:
        current = q.pop(0)
        if current in top_ordering:
            raise Exception(
                "Found a cycle! No valid topological ordering possible.")
        top_ordering.append(current)
        for neighbor in graph[current]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                q.append(neighbor)

    if len(top_ordering) != len(graph):
        raise Exception("Could not find valid topological ordering.")
    return top_ordering


def recursive_top_sort(graph):
    indegrees = {vertex: 0 for vertix in graph}
    for vertex, neighbor in graph.items():
        indegrees[neighbor] += 1

    q, top_ordering = [], []
    for vertex in graph:
        if indegrees[vertex] == 0:
            q.append(vertex)

    def helper(q):
        while q:
            current = q.pop(0)
            if current in top_ordering:
                raise Exception(
                    "Found a cycle! No valid topological ordering possible.")
            top_ordering.append(current)
            for neighbor in graph[current]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    q.append(neighbor)
    helper(q)

    if len(top_ordering) != len(graph):
        raise Exception("Could not find valid topological ordering.")

    return top_ordering
