n = int(input())
arr = []
for _ in range(n):
    x, y = input().split()
    arr.append((int(x), y))

arr.sort(key=lambda x:x[0])

for i in range(n):
    print(*arr[i])