import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = [int(input()) for _ in range(N)]

## 다른 풀이 1
start, end = max(a), sum(a)
result = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    temp = mid
    for v in a:
        if temp - v < 0:
            cnt += 1
            temp = mid
        temp -= v
    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1
        result = mid
print(result)

## 다른 풀이 2
start, end = min(a), sum(a)
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    temp = mid
    for v in a:
        if temp - v < 0:
            cnt += 1
            temp = mid
        temp -= v

    # M번 보다 더 많이 인출하거나 인출한 금액이 하루를 다 살기에 적은 경우
    if cnt > M or mid < max(a):
        start = mid + 1
    else:
        end = mid - 1
print(start)

## 내 풀이 - 틀렸음
start, end = min(a), sum(a)
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    temp = mid
    for v in a:
        if temp - v < 0:
            cnt += 1
            temp = mid
        temp -= v
    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1
print(start)