def fibonacci_sequence(n):
    fibonacci = []
    if n <= 0:
        return fibonacci
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibonacci = [0, 1]
        for i in range(2, n):
            next_fibonacci = fibonacci[i - 1] + fibonacci[i - 2]
            fibonacci.append(next_fibonacci)
        return fibonacci

