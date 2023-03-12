n = int(input())

arr = []
for _ in range(n):
    input_data = input().split()
    arr.append((input_data[0], int(input_data[1])))    # 튜플로 추가

sorted_arr = sorted(arr, key=lambda student:student[1])

for student in sorted_arr:
    print(student[0], end=' ')