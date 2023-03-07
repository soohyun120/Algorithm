import sys
sys.setrecursionlimit(10000)


n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0
result = []


def dfs(x,y):
    global count
    graph[x][y] = -1   # 방문 처리
    count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1:
                dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count = 0
            dfs(i, j)
            result.append(count)


print(len(result))
result.sort()
for k in result:
    print(k)
