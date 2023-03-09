# 특정한 데이터를 적절한 위치에 삽입
# 그 앞까지의 데이터는 이미 정렬되어 있다고 가정
# 두 번째 데이터부터 시작 (첫 번째 데이터는 그 자체로 정렬되어 있다고 판단)
# O(N^2)    ===>    거의 정렬되어 있는 경우, O(N)   "퀵정렬보다 빠름"
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)
