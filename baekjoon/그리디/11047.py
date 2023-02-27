n, k = map(int, input().split())
coin_type = []
for i in range(n):
    coin_type.append(int(input()))
coin_type.sort(reverse=True)

result = 0
for coin in coin_type:
    result += k // coin
    k %= coin

print(result)
