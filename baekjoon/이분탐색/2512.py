import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
M = int(input())

a.sort()
start, end = 1, a[-1]
while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for v in a:
        if v < mid:
            cnt += v
        else:
            cnt += mid
    if cnt <= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)