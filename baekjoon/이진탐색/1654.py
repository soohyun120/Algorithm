import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

start = 1
end = max(arr)

result = 0
while start <= end:
    mid = (start + end) // 2
    count = 0
    for v in arr:
        count += v // mid
    if count >= n:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
