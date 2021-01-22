'''
There are a total of n courses you have to take labelled from 0 to n - 1.

Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.

Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

**Example 1**

`Input: numCourses = 2, prerequisites = [[1,0]]`
`Output: [0,1]`

`Explanation`

There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

**Example 2**
`Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]`
`Output: [0,2,1,3]`

`Explanation`

There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

**Example 3**
`Input: numCourses = 1, prerequisites = []`
`Output: [0]`
'''


from collections import defaultdict


class DFSSolution:

    UNVISITED = 1
    VISITING = 2
    VISITED = 3
    FOUND_CYCLE = False

    def dfs(self, node, ordered_course, graph, visitState):
        if self.FOUND_CYCLE:
            return

        visitState[node] = DFSSolution.VISITING

        if node in graph:
            for neighbor in graph[node]:
                if visitState[neighbor] == DFSSolution.UNVISITED:
                    self.dfs(neighbor, ordered_course, graph, visitState)
                elif visitState[neighbor] == DFSSolution.VISITING:
                    self.FOUND_CYCLE = True

        visitState[node] = DFSSolution.VISITED
        ordered_course.append(node)


class GraphNode:
    def __init__(self):
        self.deps = 0
        self.prereqs = []


class Solution:
    def findOrder(self, numCourses, prerequisites):
        courses = [num for num in range(numCourses)]

        if not prerequisites:
            return courses

        g = defaultdict(GraphNode)

        for pair in prerequisites:
            current, prereq = pair
            g[current].prereqs.append(prereq)
            g[current].deps += 1
            if prereq not in g:
                g[prereq] = GraphNode()

        q = []
        for k, v in g.items():
            if v.deps == 0:
                q.append(k)

        res = []
        for course in courses:
            if course not in g.keys():
                res.append(course)

        while q:
            current = q.pop(0)
            if current not in res:
                res.append(current)
                for course, reqs in g.items():
                    if current in reqs.prereqs:
                        reqs.prereqs.remove(current)
                        reqs.deps -= 1
                        if reqs.deps == 0:
                            q.append(course)

        return res if len(res) == len(courses) else[]


class OptimalSolution(object):
    def findOrder(self, numCourses, prerequisites):
        indegree = [set() for _ in range(numCourses)]
        outdegree = [[] for _ in range(numCourses)]
        for coursePair in prerequisites:
            current, prereq = coursePair[0], coursePair[1]
            indegree[current].add(prereq)
            outdegree[prereq].append(current)
        courseOrdering, q = [], [
            i for i in range(numCourses) if not indegree[i]]
        while q:
            newStart = []
            current = q.pop(0)
            courseOrdering.append(current)
            for successor in outdegree[current]:
                indegree[successor].remove(current)
                if not indegree[successor]:
                    q.append(successor)
        return courseOrdering if len(courseOrdering) == numCourses else []
