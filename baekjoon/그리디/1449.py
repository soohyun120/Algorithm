import sys
input = sys.stdin.readline

N, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = 1
temp = arr[0] + L
for i in range(1, N):
    if temp <= arr[i]:
        result += 1
        temp = arr[i] + L

print(result)