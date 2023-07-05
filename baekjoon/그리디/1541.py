a = input().split('-')
for i in range(len(a)):
    if '+' in a[i]:
        a[i] = sum(map(int, a[i].split('+')))

a = list(map(int, a))
result = a[0]
for i in range(1, len(a)):
    result -= a[i]

print(result)
