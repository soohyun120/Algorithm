K, N = map(int, input().split())
a = [int(input()) for _ in range(K)]

start = 1
end = max(a)
while start <= end:
    mid = (start + end) // 2
    temp = 0
    for v in a:
        temp += v // mid
    if temp >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)