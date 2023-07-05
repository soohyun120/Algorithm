d = [0] * 100
d[0], d[1], d[2], d[3] = 1, 1, 1, 2
for i in range(4, 100):
    d[i] = d[i - 3] + d[i - 2]

T = int(input())
for _ in range(T):
    N = int(input())
    print(d[N - 1])