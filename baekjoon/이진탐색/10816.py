import sys
input = sys.stdin.readline

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()

dic = dict()
for v in a:
    if v not in dic:
        dic[v] = 1
    else:
        dic[v] += 1

for v in b:
    if v in dic:
        print(dic[v], end=' ')
    else:
        print(0, end=' ')