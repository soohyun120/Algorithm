# 피벗(기준)을 설정하고 그 피벗보다 큰 데이터와 작은 데이터의 위치를 바꿈
# 첫 번째 데이터를 피벗으로 설정
# 피벗을 기준으로 왼쪽 리스트, 오른쪽 리스트에서 각각 다시 정렬 수행
# 현재 리스트의 데이터 개수가 1개이면, 정렬 종료
# 평균 O(NlogN), 최악 O(N^2) ==> 이미 정렬되어 있는 경우, 매우 느리게 동작

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:    # 원소가 1개이면, 종료
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:    # 엇갈렸다면, 작은 데이터와 피벗 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:   # 엇갈리지 않았다면, 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


def quick_sort2(array):
    # 리스트가 하나 이하의 원소만 담고 있다면, 종료
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]     # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]     # 분할된 오르쪽 부분

    # 분할 이후 왼쪽 부분, 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)


quick_sort(array, 0, len(array) - 1)
print(array)

print(quick_sort2(array))


