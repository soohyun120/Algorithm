n = int(input())
f = [0] * 41

count = 1
count2 = 0

def fib(n):
    global count
    if n == 1 or n == 2:
        return 1
    else:
        count += 1
        return fib(n - 1) + fib(n - 2)

def fibonacci(n):
    global count2
    f[1], f[2] = 1, 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
        count2 += 1
    return f[n]

fib(n)
fibonacci(n)
print(count, count2)

