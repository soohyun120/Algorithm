import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    global n
    dp = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    dp[start] = 0
    while q:
        cost, now = heapq.heappop(q)
        if dp[now] < cost:
            continue
        for i in graph[now]:
            temp = dp[now] + i[1]
            if temp < dp[i[0]]:
                heapq.heappush(q, (temp, i[0]))
                dp[i[0]] = temp
    return dp

ans = dijkstra(x)
ans[0] = 0
for i in range(1, n + 1):
    if i != x:
        result = dijkstra(i)
        ans[i] += result[x]

print(max(ans))