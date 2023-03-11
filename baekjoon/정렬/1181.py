n = int(input())
arr = [input() for _ in range(n)]

# 1순위: 길이순 , 2순위: 알파벳순
arr.sort(key=lambda x: (len(x), x))

# 중복 제거
result = []
for v in arr:
    if v not in result:
        result.append(v)

for i in range(len(result)):
    print(result[i])
