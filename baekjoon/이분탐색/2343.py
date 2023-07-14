import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = list(map(int, input().split()))

start, end = max(a), sum(a)
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    temp = 0
    for v in a:
        if temp + v > mid:
            cnt += 1
            temp = 0
        temp += v
    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1
print(start)
