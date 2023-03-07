n = int(input())
arr = [[] for _ in range(11)]
for _ in range(n):
    x,y = map(int, input().split())
    arr[x].append(y)

result = 0
for cow in arr:
    if len(cow) == 0:
        continue
    temp = cow[0]
    for road_num in cow:
        if temp != road_num:
            result += 1
            temp = road_num

print(result)
