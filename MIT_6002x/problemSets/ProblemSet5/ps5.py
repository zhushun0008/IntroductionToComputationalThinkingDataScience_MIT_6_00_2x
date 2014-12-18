# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import * 
import copy
#
# Problem 2: Building up the Campus Map
# Campus Map could be modeled by an weighted graph, so buildings are
# represented by nodes in the graph, and their distance could be represented
# by its weighted edge.
#

def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    mapGraph = WeightedDigraph()
    nodeSet = set()
    edgeList = []
    print "Loading map from file..."

    with open(mapFilename) as fp:
        for line in fp:
            line = line.split()
            [src, dest, (totalDistance, distanceOutdoors)] = [Node(line[0]),
                                                              Node(line[1]),
                                                              (float(line[2]),
                                                               float(line[3]))]
            nodeSet.add(src)
            nodeSet.add(dest)
            edgeList.append(WeightedEdge(src, dest, totalDistance, distanceOutdoors))
    for node in nodeSet:
        mapGraph.addNode(node)
    for edge in edgeList:
        mapGraph.addEdge(edge)

    fp.close()
    return mapGraph



#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are
#



def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
    pass

#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#

# def DFSShortest(graph, start, end, path, shortest, maxTotalDist,
#                 maxDistOutdoors, currentTotalDist, currentTotalOutdoors,
#                 shortestTotalDist, shortestTotalOutdoors, startParent):
#     #assumes graph is a Digraph
#     #assumes start and end are nodes in graph
#     if currentTotalDist > maxTotalDist or currentTotalOutdoors > maxDistOutdoors:
#         return [None, currentTotalDist, currentTotalOutdoors]
#
#     if startParent != None:
#         startParent = Node(startParent)
#         [edgeDist, edgeDistOutdoors] = graph.getedge(startParent, start)
#         if currentTotalDist + edgeDist <= maxTotalDist and \
#                 currentTotalOutdoors + edgeDistOutdoors <= maxDistOutdoors:
#             currentTotalDist += edgeDist
#             currentTotalOutdoors += edgeDistOutdoors
#         else:
#             return [None, currentTotalDist, currentTotalOutdoors]
#
#     path = path + [start]
#
# #    print 'Current dfs path:', printPath(path)
#     if start == end:
#         return [path, currentTotalDist, currentTotalOutdoors]
#
#     start = Node(start)
#     end = Node(end)
#     for node in graph.childrenOf(start):
#         # avoid cycles
#         if str(node) not in path:
#             [newPath, totalUsedDist, totalUsedOutdoors] = DFSShortest(
#                     graph, str(node), str(end), path, shortest, maxTotalDist,
#                     maxDistOutdoors, currentTotalDist, currentTotalOutdoors,
#                     shortestTotalDist, shortestTotalOutdoors, str(start))
#             if currentTotalDist + totalUsedDist < maxDistOutdoors and \
#                     currentTotalOutdoors + totalUsedOutdoors < maxDistOutdoors:
#                 if newPath != None:
#                     currentTotalDist += totalUsedDist
#                     currentTotalOutdoors += totalUsedOutdoors
#                     if shortest == None or currentTotalDist < shortestTotalDist and \
#                                 currentTotalDist < shortestTotalOutdoors:
#                         shortest = newPath
#
#     return [shortest, currentTotalDist, currentTotalOutdoors]

# def DFSShortest(graph, start, end, path, shortest, maxTotalDist,
#                 maxDistOutdoors):
#     currentTotalDist = path[0] + path[2]
#     currentTotalOutdoors = path[1] + path[3]
#     if currentTotalDist > maxTotalDist or currentTotalOutdoors > maxDistOutdoors:
#         return None
#     tempPath = copy.deepcopy(path)
#     tempPath[0] = currentTotalDist
#     tempPath[1] = currentTotalOutdoors
#     tempPath[4] = tempPath[4] + [start]
#     start = Node(start)
#     end = Node(end)
#     # print 'Current dfs path:', printPath(path)
#     if start == end:
#         return tempPath
#     for node in graph.childrenOf(start):
#         # Avoid Cycles
#         if str(node) not in path[4]:
#             [tempPath[2], tempPath[3]] = graph.getedge(start, node)
#             if shortest == None or (tempPath[0] < shortest[0] and tempPath[1] <
#                 shortest[1]):
#                 newPath = DFSShortest(graph, str(node), str(end), tempPath,
#                                       shortest,
#                                       maxTotalDist, maxDistOutdoors)
#                 if newPath != None:
#                     shortest = newPath
#     return shortest

def getPathCost(graph, path):
    totalDistCost = 0
    totalOutdoorsCost = 0

    for i in range(len(path) - 1):
        start = Node(path[i])
        end = Node(path[i+1])
        [tempDist, tempOutdoors] = graph.getedge(start, end)
        totalDistCost += tempDist
        totalOutdoorsCost += tempOutdoors
    return [totalDistCost, totalOutdoorsCost]

# def DFSShortest(graph, start, end, visited, shortest, maxTotalDist,
#                 maxDistOutdoors):
#     #assumes graph is a Digraph
#     #assumes start and end are nodes in graph
#     path = path + [start]
# #    print 'Current dfs path:', printPath(path)
#     if start == end:
#         return path
#     start = Node(start)
#     end = Node(end)
#
#     for node in graph.childrenOf(start):
#         if str(node) not in path: #avoid cycles
#             if shortest != None:
#                 [shortestDistCost, shortestOutdoorsCost] = getPathCost(
#                         graph, shortest)
#             if path != None:
#                 [totalDistCost, totalOutdoorsCost] = getPathCost(graph, path)
#             if (shortest == None and totalDistCost < maxTotalDist and \
#                     totalOutdoorsCost < maxDistOutdoors) or (shortest != None \
#                         and totalDistCost < shortestDistCost and \
#                         totalOutdoorsCost < shortestOutdoorsCost):
#
#                 if newPath != None:
#                     shortest = newPath
#
#     return shortest

def getShortestPath(graph, start, end, maxTotalDist, maxDistOutdoors):

    start = Node(start)
    end = Node(end)
    if not (graph.hasNode(start) and graph.hasNode(end)):
        raise ValueError('Start or end not in graph.')
    path = [str(start)]

    if start == end:
        return path
    shortest = None
    currentDist = 0
    currrentOutdoors = 0
    for node in graph.childrenOf(start):
        if (str(node) not in visited or str(node) == str(end)): #avoid cycles
            [currentDist, currrentOutdoors] = graph.getedge(start, node)
            visited = visited + [str(node)] #new list
            newPath = getShortestPath(graph, node, end, visited, maxTotalDist
                                      - currentDist, maxDistOutdoors -
                                      currrentOutdoors)
            if newPath == None:
                continue
            [totalDistCost, totalOutdoorsCost] = getPathCost(graph, newPath)
            if shortest != None:
                [shortestDistCost, shortestOutdoorsCost] = getPathCost(graph,
                                                                       shortest)

            if (shortest == None and totalDistCost < maxTotalDist - \
                    currentDist and totalOutdoorsCost < maxDistOutdoors - \
                    currrentOutdoors) or (totalDistCost < shortestDistCost and
                totalOutdoorsCost < shortestOutdoorsCost):
                shortest = newPath

    if shortest != None:
        path = path + shortest
    else:
        path = None
    return path

# def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
#     """
#     Finds the shortest path from start to end using directed depth-first.
#     search approach. The total distance travelled on the path must not
#     exceed maxTotalDist, and the distance spent outdoor on this path must
# 	not exceed maxDistOutdoors.
#
#     Parameters:
#         digraph: instance of class Digraph or its subclass
#         start, end: start & end building numbers (strings)
#         maxTotalDist : maximum total distance on a path (integer)
#         maxDistOutdoors: maximum distance spent outdoors on a path (integer)
#
#     Assumes:
#         start and end are numbers for existing buildings in graph
#
#     Returns:
#         The shortest-path from start to end, represented by
#         a list of building numbers (in strings), [n_1, n_2, ..., n_k],
#         where there exists an edge from n_i to n_(i+1) in digraph,
#         for all 1 <= i < k.
#
#         If there exists no path that satisfies maxTotalDist and
#         maxDistOutdoors constraints, then raises a ValueError.
#     """
#
#
#     visited = []
#     shortestPath = getShortestPath(digraph, start, end, visited, maxTotalDist,
#                                 maxDistOutdoors)
#     if shortestPath == None:
#         raise ValueError
#     return shortestPath
#
# def printPath(path):
#     # a path is a list of nodes
#     result = ''
#     for i in range(len(path)):
#         if i == len(path[4]) - 1:
#             result = result + str(path[4][i])
#         else:
#             result = result + str(path[4][i]) + '->'
#     return result









def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
   Finds the shortest path from start to end using directed depth-first.
   search approach. The total distance travelled on the path must not
   exceed maxTotalDist, and the distance spent outdoor on this path must
        not exceed maxDisOutdoors.

   Parameters:
       digraph: instance of class Digraph or its subclass
       start, end: start & end building numbers (strings)
       maxTotalDist : maximum total distance on a path (integer)
       maxDistOutdoors: maximum distance spent outdoors on a path (integer)

   Assumes:
       start and end are numbers for existing buildings in graph

   Returns:
       The shortest-path from start to end, represented by
       a list of building numbers (in strings), [n_1, n_2, ..., n_k],
       where there exists an edge from n_i to n_(i+1) in digraph,
       for all 1 <= i < k.

       If there exists no path that satisfies maxTotalDist and
       maxDistOutdoors constraints, then raises a ValueError.
   """
    def getPathDistance(path):
        [distance, outDistance] = [0, 0]
        if path == None:
            return [maxTotalDist, maxDistOutdoors]
        for i in range(len(path)-1):
            [src, dest] = Node(path[i]), Node(path[i+1])
            [tempDist, tempOut]= digraph.getedge(src, dest)
            distance += tempDist
            outDistance += tempOut
        return [distance, outDistance]

    def DFS(start, end, path=[], shortest=None, currentDistance=0):
        path = path + [start]

        start = Node(start)
        end = Node(end)
        if start == end:
            return path
        for node in digraph.childrenOf(start):
            if str(node) not in path:
                [ShotestDistance, shortestOutDistance] = getPathDistance(shortest)
                tempPath = copy.deepcopy(path)
                path = copy.deepcopy(tempPath)
                tempPath += [str(node)]
                [currentDistance, currentOutDistance] = getPathDistance(tempPath)

                if currentDistance <= ShotestDistance and currentOutDistance <= maxDistOutdoors:
                    newPath = DFS(str(node), str(end), path, shortest,
                                  maxDistOutdoors)
                    if newPath != None:
                        shortest = copy.deepcopy(newPath)
        return shortest

    result = DFS(start, end)
    if result == None:
        raise ValueError('ValueError successfully raised')
    return result

# Uncomment below when ready to test
### NOTE! These tests may take a few minutes to run!! ####
if __name__ == '__main__':
    ## For answering Problem 02
    mitMap = load_map("testMap6.txt")
    print isinstance(mitMap, Digraph)
    print isinstance(mitMap, WeightedDigraph)
    print 'nodes', mitMap.nodes
    print 'edges', mitMap.edges


    LARGE_DIST = 1000000
    LARGE_DIST1 = 21
    LARGE_OutDoorDIST = 11
    print "Find the shortest-path from Building 2 to 9"
    expectedPath3 = ['4', '3', '5']
    dfsPath3 = directedDFS(mitMap, '4', '5', LARGE_DIST1, LARGE_OutDoorDIST)
    print "DFS: ", dfsPath3

#     Test case 1
#     print "---------------"
#     print "Test case 1:"
#     print "Find the shortest-path from Building 32 to 56"
#     expectedPath1 = ['32', '56']
#     brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
#     dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath1
#     print "Brute-force: ", brutePath1
#     print "DFS: ", dfsPath1
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)

    # Test case 2
    # print "---------------"
    # print "Test case 2:"
    # print "Find the shortest-path from Building 32 to 56 without going outdoors"
    # expectedPath2 = ['32', '36', '26', '16', '56']
    # brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
    # dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
    # print "Expected: ", expectedPath2
    # print "Brute-force: ", brutePath2
    # print "DFS: ", dfsPath2
    # print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)

#     Test case 3
#     print "---------------"
#     print "Test case 3:"
#     print "Find the shortest-path from Building 2 to 9"
#     expectedPath3 = ['2', '3', '7', '9']
#     brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#     dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath3
#     print "Brute-force: ", brutePath3
#     print "DFS: ", dfsPath3
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)

#     Test case 4
#     print "---------------"
#     print "Test case 4:"
#     print "Find the shortest-path from Building 2 to 9 without going outdoors"
#     expectedPath4 = ['2', '4', '10', '13', '9']
#     brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
#     dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
#     print "Expected: ", expectedPath4
#     print "Brute-force: ", brutePath4
#     print "DFS: ", dfsPath4
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)

#     Test case 5
#     print "---------------"
#     print "Test case 5:"
#     print "Find the shortest-path from Building 1 to 32"
#     expectedPath5 = ['1', '4', '12', '32']
#     brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#     dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath5
#     print "Brute-force: ", brutePath5
#     print "DFS: ", dfsPath5
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)

#     Test case 6
#     print "---------------"
#     print "Test case 6:"
#     print "Find the shortest-path from Building 1 to 32 without going outdoors"
#     expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
#     brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
#     dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
#     print "Expected: ", expectedPath6
#     print "Brute-force: ", brutePath6
#     print "DFS: ", dfsPath6
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)
#
# #     Test case 7
#     print "---------------"
#     print "Test case 7:"
#     print "Find the shortest-path from Building 8 to 50 without going outdoors"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
#
#     try:
#         directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         dfsRaisedErr = 'Yes'

    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did DFS search raise an error?", dfsRaisedErr

#     Test case 8
    print "---------------"
    print "Test case 8:"
    print "Find the shortest-path from Building 10 to 32 without walking"
    print "more than 100 meters in total"
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    try:
        bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
    except ValueError:
        bruteRaisedErr = 'Yes'
    
    try:
        directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
    except ValueError:
        dfsRaisedErr = 'Yes'
    
    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did DFS search raise an error?", dfsRaisedErr
