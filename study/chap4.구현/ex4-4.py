n, m = map(int, input().split())

# 방문 정보를 저장하는 맵 : 0 으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 위치 (x, y), 현재 방향 direction
x, y, direction = map(int, input().split())
# 현재 위치 방문 처리
d[x][y] = 1

# 전체 맵 정보
array = [list(map(int, input().split())) for _ in range(n)]

# 북, 동, 남, 서 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전 후 가보지 않은 칸이면, 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x,y = nx,ny
        count += 1
        turn_time = 0
        continue
    # 회전 후 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dx[direction]
        # 뒤로 갈 수 있다면, 이동
        if array[nx][ny] == 0:
            x,y = nx,ny
        # 뒤가 바다이면
        else:
            break;
        turn_time = 0

print(count)