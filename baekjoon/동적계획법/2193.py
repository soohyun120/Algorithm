N = int(input())

d = [0] * 90
d[0], d[1] = 1, 1
for i in range(2, N):
    d[i] = d[i - 2] + d[i - 1]

print(d[N - 1])