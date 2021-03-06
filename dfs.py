class NodeInfo(object):
    """
    Represents information about a node that can be found
    during a depth-first search
    """
    
    def __init__(self, id):
        self.nodeID = id
        self.connectedComponentID = None
        self.preClock = None
        self.postClock = None


# this is just a helper function that I found convenient
def numNodes(g):
    """returns the number of vertexes in the graph
    g which is represented by adjacency lists
    (max of the len(g) and the max neighbor + 1)
    """
    return max(len(g), 1 + max(t for ts in g for t in ts))


# TODO: implement this
def reverseGraph(g):
    """ Given a graph g represented in adjacency list
    representation, returns a graph r such that:
    s,t in g <=> t,s in r
    """
    n=numNodes(g)
    newlist = list(list() for _ in range(n))
    for Source in range(0, len(g)):
        node=g[Source]
        for Target in node:
            newlist[Target].append(Source)
    return newlist


# TODO: implement this
def depthFirstSearch(g, visitOrder=None):
    """ Given a graph g represented in adjacency list
    representation, returns a list of NodeInfo objects
    containing node index, preClock, postClock, and connectedComponentID (connected compoent ids),
    sorted in reverse order of postClock
    args:
        g: graph as adjacency list (list at index i are the outgoing neighbors of node i)
        visitOrder: the order in which to attempt to explore nodes;
            the default is to compute this order to be the reverse order
            of postClock times in the reverse graph under an arbitrary
            visitOrder.  Such a visit order produces connectedComponentIDs that are
            the strongly connected components of g and are in reverse
            topological order.
    """
    NumNodes= numNodes(g)
    if visitOrder is None:
        visitOrder=[]
        for node in depthFirstSearch(reverseGraph(g),range(NumNodes)):
            visitOrder.append(node.nodeID)
    
    counter = 0
    clock = 0
    nodes = list(NodeInfo(ID) for ID in range(NumNodes))
    result = []
    visited= [False] * NumNodes

    def explore(i:int):
        nonlocal clock
        visited[i]=True
        nodes[i].connectedComponentID= counter
        nodes[i].preClock = clock
        clock += 1
        #g at i is a list of out neighbors
        if i<len(g):
            for neighborIndex in g[i]:
                if not visited[neighborIndex]:
                    explore(neighborIndex)
        nodes[i].postClock = clock
        clock += 1
        result.append(nodes[i])
            
    for i in visitOrder:
        if not visited[i]:
            explore(i)
            counter+=1

    result.reverse()
    
    return result
