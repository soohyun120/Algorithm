n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n
dp2 = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

arr.reverse()

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

dp2.reverse()

for i in range(n):
    dp[i] = dp[i] + dp2[i]

print(max(dp) - 1)