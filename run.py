# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
ou = search.GPSProblem('O', 'U', search.romania)
th = search.GPSProblem('T', 'H', search.romania)


#print(search.breadth_first_graph_search(ab).path())
#print(search.depth_first_graph_search(ab).path())

print("De A a B")
print("Sin Heuristica")
print(search.branch_and_bound_graph_search(ab).path())
print("Con Heuristica")
print("Path: " + str(search.branch_and_bound_subestimate_graph_search(ab).path()))
print("============================================================")


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
