import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))
a.sort()

dic = {}
for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

## 다른 풀이
for v in b:
    if v in dic:
        print(dic[v], end=' ')
    else:
        print(0, end=' ')

## 내 풀이
for v in b:
    result = 0
    if a[0] <= v <= a[-1]:
        start, end = 0, N - 1
        while start <= end:
            mid = (start + end) // 2
            if v == a[mid]:
                result = 1
                break
            if v > a[mid]:
                start = mid + 1
            else:
                end = mid - 1
    if result:
        print(dic[v], end=' ')
    else:
        print(0, end=' ')