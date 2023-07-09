N, M = map(int, input().split())
a = list(map(int, input().split()))

result = 0
for i in range(0, N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            temp = a[i] + a[j] + a[k]
            if result < temp <= M:
                result = temp
print(result)