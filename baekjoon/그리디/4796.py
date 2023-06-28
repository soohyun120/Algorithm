import sys
input = sys.stdin.readline

cnt = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break

    result = V // P * L + min(V % P, L)  # 남은 일수(V%P) 가 L보다 큰 경우도 고려
    print("Case {}: {}".format(cnt, result))
    cnt += 1