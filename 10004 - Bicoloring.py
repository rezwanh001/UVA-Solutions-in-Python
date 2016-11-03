from collections import deque

def Main():
    while True:
        N = int(input())
        if N == 0: break
        M = int(input())
        graph = [[0 for y in range(N)] for x in range(N)]
        color = [-1]*N

        for i in range(M):
            a,b = map(int ,input().split())
            graph[a][b] = 1
            graph[b][a] = 1

        q = deque([0])
        color[0] = 0
        flag = True

        while q:
            u = q.popleft()
            for v in range(N):
                if not graph[u][v]:
                    continue
                if color[v] == -1:
                    color[v] = color[u] + 1
                    q.append(v)

                elif color[u] == color[v] :
                    flag = False
                    break
            if not flag :
                break

        if flag:
            print("BICOLORABLE.")
        else:
            print('NOT BICOLORABLE.')

if __name__ == '__main__':
    Main()