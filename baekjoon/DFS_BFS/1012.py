import sys
sys.setrecursionlimit(10000)    # 런타임 에러 방지


def dfs(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if d[nx][ny] == 1:
                d[nx][ny] = -1  # 방문 처리
                dfs(nx,ny)

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    d = [[0] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        d[x][y] = 1

    result = 0
    for i in range(n):
        for j in range(m):
            if d[i][j] > 0:
                dfs(i, j)
                result += 1

    print(result)
