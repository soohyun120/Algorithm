import sys
input = sys.stdin.readline

## Set : search -> O(1)
N = int(input())
a = set(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))

for v in b:
    if v in a:
        print(1)
    else:
        print(0)

## 내 풀이 - 시간 초과
## 이유 : min(a), max(a) -> O(N)
N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))

a.sort()
for v in b:
    result = 0
    # if min(a) <= v <= max(a):
    if a[0] <= v <= a[-1]:
        start, end = 0, N - 1
        while start <= end:
            mid = (start + end) // 2
            if v == a[mid]:
                result = 1
                break
            elif v < a[mid]:
                end = mid - 1
            else:
                start = mid + 1
    print(result)