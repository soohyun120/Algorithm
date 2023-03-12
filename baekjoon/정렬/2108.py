import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

print(round(sum(arr) / n))  # 소수 첫 번째 자리 반올림

arr.sort()
print(arr[n // 2])   # 중앙값

# 최빈값
dic = dict()
for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
mx = max(dic.values())
max_arr = []

for i in dic:
    if mx == dic[i]:
        max_arr.append(i)

if len(max_arr) > 1:
    print(max_arr[1])
else:
    print(max_arr[0])

# 범위: 최댓값 - 최솟값
print(max(arr) - min(arr))