from collections import defaultdict
from collections import deque
from pprint import pprint
visited = {}
result = deque()
graph = defaultdict(list)

def topoVisit(u):
    visited[u] = 1
    for v in graph[u]:
        if not visited[v]:
            topoVisit(v)
    result.append(u)

def topoSort(nodes, graph):
    for v in nodes:
        visited[v] = 0

    for v in nodes:
        if not visited[v]:
            topoVisit(v)

    result.reverse()
    # return result
    print(' '.join([str(e) for e in result]))

def topolgical_sort(graph_unsorted):

    graph_sorted = []

    graph_unsorted = dict(graph_unsorted)

    while graph_unsorted:
        acyclic = False
        for node, edges in graph_unsorted.items():
            for edge in edges:
                if edge in graph_unsorted:
                    break
            else:
                acyclic = True
                del graph_unsorted[node]
                graph_sorted.append((node, edges))

        if not acyclic:
            raise RuntimeError("A cyclic dependency occurred")

    return graph_sorted

def dfs(i, countrd, ans):
    ans = []
    ans.append(i)
    countrd[i] -= 1
    for j in i.neighbors:
        countrd[j] = countrd[j] - 1
        if countrd[j] == 0:
            dfs(j, countrd, ans)
def topSort1(graph):
        # write your code here
    countrd = {}
    for x in graph:
        countrd[x] = 0

    for i in graph:
        for j in i.neighbors:
            countrd[j] = countrd[j] + 1

    ans = []
    for i in graph:
        if countrd[i] == 0:
            dfs(i, countrd, ans)
    return ans

if __name__ == '__main__':
    # while True:
    #     n,m = map(int,input().split())
    #     if n == 0 and m == 0:
    #         break
    #
    #     # nodes = list(range(1,n+1))
    #     for i in range(m):
    #         v1,v2 = map(int,input().split())
    #         graph[v1].append(v2)

    graph= [(2, []),
                  (5, [11]),
                  (11, [2, 9, 10]),
                  (7, [11, 8]),
                  (9, []),
                  (10, []),
                  (8, [9]),
                  (3, [10, 8])]
    # m = 4
    # for i in range(m):
    #     v1,v2 = map(int,input().split())
    #     graph[v1].append(v2)

    pprint(topSort1(graph))
    # print(*A)
