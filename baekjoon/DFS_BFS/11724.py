import sys
sys.setrecursionlimit(5000)     # 런타임 에러 (재귀 제한)
input = sys.stdin.readline      # 시간 초과

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

result = 0
visited = [False] * (n+1)


for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        result += 1

print(result)
