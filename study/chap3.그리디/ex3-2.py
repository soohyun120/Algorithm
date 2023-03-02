n, m, k = map(int, input().split())
d = list(map(int, input().split()))

d.sort()
first = d[n - 1]    # 가장 큰 수
second = d[n - 2]   # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += count * first         # 가장 큰 수 더하기
result += (m-count) * second    # 두 번째로 큰 수 더하기

print(result)