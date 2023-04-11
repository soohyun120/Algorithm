n = int(input())
arr = list(map(int, input().split()))
d1 = [1] * n
d2 = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            d1[i] = max(d1[i], d1[j] + 1)

arr.reverse()

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            d2[i] = max(d2[i], d2[j] + 1)

d2.reverse()

for i in range(n):
    d1[i] = d1[i] + d2[i]

print(max(d1) - 1)
