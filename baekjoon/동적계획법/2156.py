n = int(input())
arr = [0] * 10001
for i in range(1, n + 1):
    arr[i] = int(input())

dp = [0] * 10001
dp[1] = arr[1]
dp[2] = arr[1] + arr[2]
for i in range(3, n + 1):
    dp[i] = max(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i], dp[i - 1])

print(dp[n])