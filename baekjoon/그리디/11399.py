n = int(input())
d = list(map(int, input().split()))

d.sort()

result = 0
sum_value = 0
for time in d:
    sum_value += time
    result += sum_value

print(result)