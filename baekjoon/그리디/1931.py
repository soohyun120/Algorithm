import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key=lambda x: (x[1], x[0]))

result = 1
end = arr[0][1]
for i in range(1, N):
    if end <= arr[i][0]:
        result += 1
        end = arr[i][1]

print(result)