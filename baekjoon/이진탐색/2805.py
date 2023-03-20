import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

start = 0
end = arr[-1] - 1

while start <= end:
    mid = (start + end) // 2
    total = 0
    for v in arr:
        if v > mid:
            total += v - mid
    if total >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)