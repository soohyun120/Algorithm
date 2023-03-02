n = int(input())
road_len = list(map(int, input().split()))
oil_price = list(map(int, input().split()))

result = 0
c = oil_price[0]
for i in range(n-1):
    if c > oil_price[i]:
        c = oil_price[i]
    result += c * road_len[i]

print(result)