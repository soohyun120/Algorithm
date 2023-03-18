import sys
input = sys.stdin.readline

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return None

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()

for v in b:
    if binary_search(a, v, 0, n - 1) != None:
        print("1")
    else:
        print("0")