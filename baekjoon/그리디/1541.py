a = input().split('-')

b = []
for i in a:
    j = i.split('+')
    sum_value = 0
    for k in j:
        sum_value += int(k)
    b.append(sum_value)

result = b[0]
for i in range(1, len(b)):
    result -= int(b[i])

print(result)