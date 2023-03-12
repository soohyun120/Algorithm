## 이진 탐색으로 풀기
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
items = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))

for i in range(len(arr)):
    result = binary_search(items, arr[i], 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')


## count sort로 풀기
n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] += 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

## set 자료형으로 풀기
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')