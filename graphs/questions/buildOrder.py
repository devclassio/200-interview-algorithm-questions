'''
CTCI, Page 110, Trees and Graphs
You are given a list of projects and a list of deps.
All of a projects deps must be built before the project.
Find a build order that will allow the projects to be built.
If there is no valid err return None.

Input:
projects -> a, b, c, d, e, f
deps -> (a, d), (f, b), (b, d), (f, a), (d, c)
'''
