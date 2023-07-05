N = int(input())
a = list(map(int, input().split()))
a.sort()

result = 0
for v in a:
    result += N * v
    N -= 1

print(result)