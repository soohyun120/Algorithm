N = int(input())

result = 1000000
for i in range(1, N + 1):
    num = sum(map(int, str(i))) #각 자릿수 더하기
    if i + num == N: #분해합
        print(i)
        break
    if i == N:
        print(0)
