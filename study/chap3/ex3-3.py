n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))

    # 현재 행에서 가장 작은 수
    min_value = min(data)

    # 가장 작은 수들 중에서 가장 큰 수
    result = max(result, min_value)

print(result)