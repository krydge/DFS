from typing import List
def old_depthFirstSearch(graph:List[List[int]]):
    counter = 0
    result = [-1]*len(graph)
    visited= [False] * len(graph)

    def explore(i:int):
        visited[i]=True
        result[i]= counter

        for neighborIndex in graph[i]:
            if not visited[neighborIndex]:
                explore(neighborIndex)
            
    for i in range(len(graph)):
        if not visited[i]:
            explore(i)
            counter+=1

    return result



class SearchNode(object):
    def __init__(self):
        self.connectedComponentID = None
        self.preClockIndex = None
        self.postClockIndex = None
        self.isVisited = False


#return list of search node in topilogical order
#where each searchnode  has id, pre and post clock time and connected component id
def depthFirstSearch(graph:List[List[int]]) -> List[SearchNode]:
    counter = 0
    clock = 0
    nodes = list(SearchNode() for _ in range(len(graph)))
    result = []

    def explore(i:int):
        nonlocal clock
        nodes[i].isVisited=True
        nodes[i].connectedComponentID= counter
        nodes[i].preClockIndex = clock
        clock += 1

        for neighborIndex in graph[i]:
            if not nodes[neighborIndex].isVisited:
                explore(neighborIndex)
        nodes[i].postClockIndex = clock
        clock += 1
        result.append(nodes[i])
            
    for i in range(len(graph)):
        if not nodes[i].isVisited:
            explore(i)
            counter+=1

    result.reverse()
    return result


def test_dfs():
    stuff = list(n.connectedComponentID for n in depthFirstSearch(
        [[1,2],
        [0],
        [0],
        [4],
        [3]]))
    assert stuff==[1,1,0,0,0]

def test_preclock():
    stuff = list(n.preClockIndex for n in depthFirstSearch(
        [[1,2],
        [0],
        [0],
        [4],
        [3]]))
    assert stuff == [6,7,0,3,1]