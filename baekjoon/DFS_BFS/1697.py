from collections import deque

n, k = map(int, input().split())

MAX = 100001
array = [0] * (MAX + 1)

def bfs():
    queue = deque([n])
    while queue:
        x = queue.popleft()
        if x == k:
            return array[x]
        for nx in (x - 1, x + 1, 2 * x):
            if 0 <= nx < MAX and not array[nx]:
                array[nx] = array[x] + 1
                queue.append(nx)

print(bfs())