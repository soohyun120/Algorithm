import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(graph, d):
    n = len(graph)
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    d[0][0] = graph[0][0]
    while q:
        cost, x, y = heapq.heappop(q)
        if d[x][y] < cost:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                next_cost = cost + graph[nx][ny]
                if next_cost < d[nx][ny]:
                    heapq.heappush(q, (next_cost, nx, ny))
                    d[nx][ny] = next_cost
    return d[n-1][n-1]

num = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = [[] for _ in range(n)]
    d = [[INF] * n for _ in range(n)]
    graph = [list(map(int, input().split())) for _ in range(n)]

    ans = dijkstra(graph, d)
    print('Problem {}: {}'.format(num, ans))
    num += 1