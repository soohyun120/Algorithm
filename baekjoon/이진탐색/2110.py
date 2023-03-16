import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

start = 1   # 최소 거리
end = arr[-1] - arr[0]  # 최대 거리

result = 0
while start <= end:
    mid = (start + end) // 2
    current = arr[0]
    count = 1
    for i in range(1, len(arr)):
        if arr[i] >= current + mid:
            count += 1
            current = arr[i]
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
