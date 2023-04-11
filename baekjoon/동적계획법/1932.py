import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    arr[i][0] = arr[i][0] + arr[i - 1][0]
    for j in range(1, len(arr[i]) - 1):
        arr[i][j] = max(arr[i - 1][j - 1], arr[i - 1][j]) + arr[i][j]
    arr[i][len(arr[i]) - 1] = arr[i - 1][len(arr[i]) - 2] + arr[i][len(arr[i]) - 1]

print(max(arr[n - 1]))
