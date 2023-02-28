n = int(input())
time_table = []
for i in range(n):
    time_table.append(tuple(map(int, input().split())))

# 1.끝나는 시간 오름차순  2.시작 시간 오름차순
time_table.sort(key=lambda x:(x[1], x[0]))

result = 1
end_time = time_table[0][1]
for i in range(1, n):
    if time_table[i][0] >= end_time:
        result += 1
        end_time = time_table[i][1]

print(result)

