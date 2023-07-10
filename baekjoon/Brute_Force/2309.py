a = [int(input()) for _ in range(9)]
x, y = 0, 0
for i in range(9):
    for j in range(i + 1, 9):
        if sum(a) - a[i] - a[j] == 100:
            # a[i], a[j] = 0, 0
            x, y = a[i], a[j]

a.remove(x)
a.remove(y)

a.sort()
for v in a:
    # if v != 0:
    #     print(v)
    print(v)