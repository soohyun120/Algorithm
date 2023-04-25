import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
d = [INF] * (n + 1)

def dijkstra(start, k):
    q = []
    heapq.heappush(q, (0, start))
    d[start] = 0
    while q:
        cost, now = heapq.heappop(q)
        if d[now] < cost:
            continue
        for i in graph[now]:
            next_cost = d[now] + i[1]
            if next_cost < d[i[0]]:
                heapq.heappush(q, (next_cost, i[0]))
                d[i[0]] = next_cost

    if k not in d:
        print(-1)
        return
    for i in range(n + 1):
        if d[i] == k:
            print(i)

dijkstra(x, k)