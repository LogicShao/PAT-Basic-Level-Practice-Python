def Fibonacci_recursion(n):
    if n == 1 or n == 2:
        return 1
    a = Fibonacci_recursion(n - 1)
    b = Fibonacci_recursion(n - 2)
    return a + b


def Fibonacci_loop(n):
    fib = [1, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib


if __name__ == '__main__':
    n = 20
    print('递归法：')
    for i in range(1, n + 1, 10):
        print(''.join(map('{:5}'.format,
              (Fibonacci_recursion(i + j) for j in range(10)))))
    print('循环法：')
    fib = Fibonacci_loop(n)
    for i in range(1, n + 1, 10):
        print(''.join(map('{:5}'.format,
              (fib[i + j - 1] for j in range(10)))))
