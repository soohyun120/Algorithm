import sys
input = sys.stdin.readline

k, n = map(int, input().split())
a = [int(input()) for _ in range(k)]

start = 1
end = max(a)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in a:
        total += x // mid
    if total >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)