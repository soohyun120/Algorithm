N = int(input())
km = list(map(int, input().split()))
won = list(map(int, input().split()))

result = 0
for i in range(N - 1):
    if won[i] < won[i + 1]:
        won[i + 1] = won[i]
    result += won[i] * km[i]

print(result)