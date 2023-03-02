n, k = map(int, input().split())

result = 0
while True:
    # 1번 과정
    target = (n // k) * k
    result += (n - target)
    n = target

    # 더 이상 나눌 수 없을 때
    if n < k:
        break

    # 2번 과정
    result += 1
    n //= k

# 1번 과정 : 마지막 1로 만들기
result += (n - 1)
print(result)
