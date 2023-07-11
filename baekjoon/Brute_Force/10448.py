## 다른 풀이
t = [n * (n + 1) // 2 for n in range(1, 46)]
eur = [0] * 1001

# 모든 유레카 수를 미리 구하기
for i in t:
    for j in t:
        for k in t:
            if i + j + k <= 1000:
                eur[i + j + k] = 1

T = int(input())
for _ in range(T):
    print(eur[int(input())])

## 내 풀이
T = int(input())
a = [int(input()) for _ in range(T)]

t = []
for i in range(1, 45):
    t.append(i * (i + 1) // 2)

for i in range(T):
    result = 0
    for j in range(44):
        for k in range(44):
            for l in range(44):
                if t[j] + t[k] + t[l] == a[i]:
                    result = 1
                    break
            if result:
                break
        if result:
            break
    print(result)