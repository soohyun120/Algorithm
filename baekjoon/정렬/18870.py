import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
sorted_arr = list(sorted(set(arr)))

dic = {sorted_arr[i] : i for i in range(len(sorted_arr))}

for v in arr:
    print(dic[v], end=' ')