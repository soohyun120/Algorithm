n = int(input())
arr = [0] * 10001
for i in range(1, n + 1):
    arr[i] = int(input())

d = [0] * 10001
d[1] = arr[1]
d[2] = arr[1] + arr[2]
for i in range(3, n + 1):
    d[i] = max(d[i - 3] + arr[i - 1] + arr[i], d[i - 2] + arr[i], d[i - 1])

print(d[n])