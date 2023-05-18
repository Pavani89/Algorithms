'''
Write a Python function that takes a number n as input and returns the nth term in the Fibonacci sequence.
'''
# 0 1 1 2 3 5 8 13 21 34 55

def fibonacci(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

# Test the function
n = 7
result = fibonacci(n)
print(result)  # Output: 8