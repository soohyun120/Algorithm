from collections import deque

n, m, v = map(int, input().split())

graph = []
for i in range(n+1):
    graph.append([])
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(n+1):
    graph[i].sort()

dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)

def dfs(graph, v, visited):
    visited[v] = True
    dfs_result.append(v)
    for k in graph[v]:
        if not visited[k]:
            dfs(graph, k, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        x = queue.popleft()
        bfs_result.append(x)
        for k in graph[x]:
            if not visited[k]:
                queue.append(k)
                visited[k] = True

dfs_result = []
bfs_result = []

dfs(graph, v, dfs_visited)
bfs(graph, v, bfs_visited)

# 리스트 한 번에 출력
print(*dfs_result)
print(*bfs_result)

