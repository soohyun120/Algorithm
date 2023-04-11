n = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(n)])

d = [1] * n
for i in range(n):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            d[i] = max(d[i], d[j] + 1)

print(n - max(d))
