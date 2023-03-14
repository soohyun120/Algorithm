import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 1
end = max(arr)

while start <= end:
    count = 0
    mid = (start + end) // 2
    for x in arr:
        if x > mid:
            count += x - mid
        if count > m:   # 절단된 나무의 길이가 m보다 길면 중단
            break
    if count >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)