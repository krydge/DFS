from dfs import depthFirstSearch, reverseGraph

# # Note you can use the following code to draw the example graphs
# # if you want (you'll need to pip install networkx and matplotlib)
# import networkx as nx
# from matplotlib import pyplot as plt

# def draw_graph(graph):
#     """
#     optional function that uses networkx and matplotlib to draw the
#     graphs

#     # e.g. the following should pop up a window with a drawing of
#     # the graph in figure 3.9a of the book:
#     draw_graph(fig3_9_a())

#     """
#     edges = list((s, t) for s, ts in enumerate(graph) for t in ts)
#     returnGraph = nx.DiGraph(edges)
#     nx.draw_networkx(returnGraph)
#     plt.show()


def fig3_9_a():
    """Builds the directed graph from figure 3.9.a on page 91 of Algorithms book"""
    g = list([] for _ in range(12))
    g[0].extend([1])
    g[1].extend([2, 3, 4])
    g[2].extend([5])
    g[3].extend([])
    g[4].extend([1, 5, 6])
    g[5].extend([2, 7])
    g[6].extend([7, 9])
    g[7].extend([10])
    g[8].extend([6])
    g[9].extend([8])
    g[10].extend([11])
    g[11].extend([9])
    return g


def test_reverse1():
    r = reverseGraph([[2, 3], [2], [1, 4]])
    assert r == [[], [2], [0, 1], [0], [2]]


def test_reverse2():
    r = reverseGraph(fig3_9_a())
    expected = list([] for _ in range(12))
    expected[1].extend([0, 4])
    expected[2].extend([1, 5])
    expected[3].extend([1])
    expected[4].extend([1])
    expected[5].extend([2, 4])
    expected[6].extend([4, 8])
    expected[7].extend([5, 6])
    expected[8].extend([9])
    expected[9].extend([6, 11])
    expected[10].extend([7])
    expected[11].extend([10])
    assert r == expected


def test_dfs1():
    result = depthFirstSearch([[2, 3], [2], [1, 4]], visitOrder=range(5))
    nodeIDs = list(n.nodeID for n in result)
    assert nodeIDs == [0, 3, 2, 4, 1]

    preClocks = list(n.preClock for n in result)
    assert preClocks ==  [0, 7, 1, 4, 2]

    postClocks = list(n.postClock for n in result)
    assert postClocks == [9, 8, 6, 5, 3] 


def test_dfs1b():
    result = depthFirstSearch([[2, 3], [2], [1, 4]])
    nodeIDs = list(n.nodeID for n in result)
    assert nodeIDs == [0, 1, 2, 3, 4]

    preClocks = list(n.preClock for n in result)
    assert preClocks ==  [8, 4, 5, 2, 0]

    postClocks = list(n.postClock for n in result)
    assert postClocks == [9, 7, 6, 3, 1]

    componentIDs = list(n.connectedComponentID for n in result)
    assert componentIDs == [3, 2, 2, 1, 0]


def test_dfs2():
    result = depthFirstSearch([
        [1, 2],
        [0], 
        [0],
        [4],
        [3],
    ], visitOrder=range(5))
    nodeIDs = list(n.nodeID for n in result)
    assert nodeIDs == [3, 4, 0, 2, 1]

    componentIDs = list(n.connectedComponentID for n in result)
    preClocks = list(n.preClock for n in result)
    assert preClocks == [6, 7, 0, 3, 1]
    
    postClocks = list(n.postClock for n in result)
    assert postClocks == [9, 8, 5, 4, 2]

    componentIDs = list(n.connectedComponentID for n in result)
    assert componentIDs == [1, 1, 0, 0, 0]


def test_dfs2b():
    result = depthFirstSearch([
        [1, 2],
        [0], 
        [0],
        [4],
        [3],
    ])
    nodeIDs = list(n.nodeID for n in result)
    assert nodeIDs == [0, 2, 1, 3, 4]

    componentIDs = list(n.connectedComponentID for n in result)
    preClocks = list(n.preClock for n in result)
    assert preClocks == [4, 7, 5, 0, 1]
    
    postClocks = list(n.postClock for n in result)
    assert postClocks == [9, 8, 6, 3, 2]

    componentIDs = list(n.connectedComponentID for n in result)
    assert componentIDs == [1, 1, 1, 0, 0] 


def test_dfs3():
    result = depthFirstSearch(fig3_9_a())
    nodeIDs = list(n.nodeID for n in result)
    assert nodeIDs == [0, 1, 4, 2, 5, 3, 6, 7, 10, 11, 9, 8]

    componentIDs = list(n.connectedComponentID for n in result)
    preClocks = list(n.preClock for n in result)
    assert preClocks == [22, 18, 19, 14, 15, 12, 0, 1, 2, 3, 4, 5]
    
    postClocks = list(n.postClock for n in result)
    assert postClocks == [23, 21, 20, 17, 16, 13, 11, 10, 9, 8, 7, 6]

    componentIDs = list(n.connectedComponentID for n in result)
    assert componentIDs == [4, 3, 3, 2, 2, 1, 0, 0, 0, 0, 0, 0]
