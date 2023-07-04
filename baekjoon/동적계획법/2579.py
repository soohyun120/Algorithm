n = int(input())
a = [0] * 301
for i in range(n):
    a[i] = int(input())

d = [0] * 301
d[0] = a[0]
d[1] = a[0] + a[1]
d[2] = max(a[0] + a[2], a[1] + a[2])
for i in range(3, n):
    d[i] = max(d[i - 3] + a[i - 1] + a[i], d[i - 2] + a[i])

print(d[n - 1])