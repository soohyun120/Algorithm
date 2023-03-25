import sys
input = sys.stdin.readline

def fib_recur(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_recur(n - 1) + fib_recur(n - 2)

def fib_dp(n):
    d = [0] * (n + 1)
    d[1], d[2] = 1, 1
    count = 0
    for i in range(3, n + 1):
        d[i] = d[i - 1] + d[i - 2]
        count += 1
    return count

n = int(input())
print(fib_recur(n), fib_dp(n))
