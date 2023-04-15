import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().split())
dp = [INF] * 100001

def dijkstra(n, k):
    if k <= n:
        return n - k
    q = []
    heapq.heappush(q, (0, n))
    while q:
        cost, pos = heapq.heappop(q)
        for i in [pos + 1, pos - 1, pos * 2]:
            if 0 <= i <= 100000:
                if i == pos * 2 and dp[i] == INF:
                    heapq.heappush(q, (cost, i))
                    dp[i] = cost
                elif dp[i] == INF:
                    heapq.heappush(q, (cost + 1, i))
                    dp[i] = cost + 1
    return dp[k]

print(dijkstra(n, k))