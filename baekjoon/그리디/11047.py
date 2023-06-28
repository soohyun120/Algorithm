import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)

result = 0
for v in arr:
    result += K // v
    K %= v

print(result)
