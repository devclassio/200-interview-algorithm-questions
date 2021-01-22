'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

**Example 1**

`Input: numCourses = 2, prerequisites = [[1,0]]`
`Output: true`

Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

**Example 2**
`Input: numCourses = 2, prerequisites = [[1,0],[0,1]]`
`Output: false`

Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should
also have finished course 1. So it is impossible.

**Note**
You may assume that there are no duplicate edges in the input prerequisites.
'''

from collections import defaultdict


class Solution(object):
    def __init__(self):
        self.eligibleCourses = []
        self.visited = []

    def seedEligibleCourses(self, g):
        for index, node in g.items():
            if len(node) == 0 and index not in self.visited:
                self.eligibleCourses.append(index)

    def dfs(self, node, g):
        if node in self.visited:
            return

        self.visited.append(node)
        for _, n in g.items():
            if node in n:
                n.remove(node)

        for successor in g[node]:
            if successor not in self.visited:
                self.eligibleCourses.append(successor)
                self.dfs(node, g)

    def canFinish(self, numCourses, prerequisites):
        if not prerequisites:
            return True

        graph = defaultdict(list)
        for relation in prerequisites:
            currentCourse, prerequisite = relation[0], relation[1]
            graph[prerequisite].append(currentCourse)  # post order!!
            if currentCourse not in graph:
                graph[currentCourse] = []

        self.seedEligibleCourses(graph)
        while self.eligibleCourses:
            current = self.eligibleCourses.pop(0)
            self.dfs(current, graph)
            self.seedEligibleCourses(graph)

        for _, n in graph.items():
            if len(n) > 0:
                return False
        return True
