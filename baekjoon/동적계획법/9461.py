T = int(input())
n = [int(input()) for _ in range(T)]

for i in range(T):
    d = [0] * 101
    d[1], d[2], d[3], d[4], d[5] = 1, 1, 1, 2, 2
    for j in range(6, n[i] + 1):
        d[j] = d[j - 1] + d[j - 5]

    print(d[n[i]])

