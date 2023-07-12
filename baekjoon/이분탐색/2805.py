import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = list(map(int, input().split()))

start, end = 0, max(a)
while start <= end:
    mid = (start + end) // 2
    target = 0
    for v in a:
        if v > mid:
            target += v - mid
        if target >= M:     # 자른 나무들의 합이 m을 넘어가면 안됨
            break
    if target >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
