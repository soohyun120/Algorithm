import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
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
for i in a:
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1

for i in b:
    if binary_search(a, i, 0, n - 1) != None:
        print(dic[i], end=' ')
    else:
        print(0, end=' ')
